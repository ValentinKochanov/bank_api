from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from .services import replenishment_card, outlay_master_account, outlay_account, validate
from .models import Customer, Account, Replenishment, Outlay
from .serializers import (CustomerSerializer,
                          AccountSerializer,
                          AccountCardSerializer,
                          ReplenishmentSerializer,
                          OutlaySerializer)


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class AccountBalance(APIView):
    """Получить баланс карты по номеру"""
    def get(self, request):
        serializer = AccountCardSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = AccountCardSerializer(request.data)
        validate(self, serializer.data['card'])
        account = Account.objects.get(card=serializer.data['card'])
        return Response(account.balance)


class ReplenishmentView(APIView):
    """Зачисление на карту по номеру"""
    def get(self, request):
        serializer = ReplenishmentSerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = ReplenishmentSerializer(data=request.data)
        if serializer.is_valid():
            data_card = serializer.data['card']
            data_amount = serializer.data['amount']
            validate(self, data_card)
            outlay_master_account(self, data_amount)
            replenishment_card(data_card, data_amount)
            Replenishment.objects.create(card=data_card, amount=data_amount)
            return Response()


class OutlayView(APIView):
    """Списание с карты по номеру"""
    def get(self, request):
        serializer = OutlaySerializer()
        return Response(serializer.data)

    def post(self, request):
        serializer = OutlaySerializer(data=request.data)
        if serializer.is_valid():
            data_card = serializer.data['card']
            data_amount = serializer.data['amount']
            validate(self, data_card)
            outlay_account(data_card, data_amount)
            Outlay.objects.create(card=data_card, amount=data_amount,
                                  INN=serializer.data['INN'])
            return Response()
