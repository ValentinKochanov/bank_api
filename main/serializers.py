from rest_framework import serializers
from .models import Customer, Account, Replenishment, Outlay


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class AccountCardSerializer(serializers.Serializer):
    card = serializers.IntegerField()


class ReplenishmentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Replenishment
        fields = '__all__'


class OutlaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Outlay
        fields = '__all__'
