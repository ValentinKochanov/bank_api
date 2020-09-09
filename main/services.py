import decimal
from rest_framework import serializers

from .models import Account, Master_Account


def validate(self, value):
    """Проверяем, что карта с таким номером есть в базе"""
    try:
        Account.objects.get(card=value)
    except:
        raise serializers.ValidationError("Карта не найдена")


def replenishment_card(data_card, data_amount):
    """Выбор карты из базы по номеру, пополнение на указанную сумму"""
    account = Account.objects.get(card=data_card)
    account.balance += decimal.Decimal(data_amount)
    account.save()


def outlay_master_account(self, data_amount):
    """Списание с мастер-счёта указанной суммы перед внесением её на карту"""
    master_account = Master_Account.objects.get(pk=1)
    if decimal.Decimal(data_amount) <= 0:
        raise serializers.ValidationError("Сумма пополнения должна быть больше нуля")
    if master_account.balance >= decimal.Decimal(data_amount):
        master_account.balance -= decimal.Decimal(data_amount)
        master_account.save()
    else:
        raise serializers.ValidationError("Недостаточно средств на мастер-счёте")


def outlay_account(data_card, data_amount):
    """Выбор карты из базы по номеру, списание указанной суммы"""
    account = Account.objects.get(card=data_card)
    if decimal.Decimal(data_amount) <= 0:
        raise serializers.ValidationError("Сумма списания должна быть больше нуля")
    if account.balance >= decimal.Decimal(data_amount):
        account.balance -= decimal.Decimal(data_amount)
        account.save()
    else:
        raise serializers.ValidationError("Недостаточно средств на счёте")
