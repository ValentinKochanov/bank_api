from django.db import models


class Customer(models.Model):
    """Пользователь"""
    id = models.PositiveSmallIntegerField(primary_key=True)
    FIO = models.CharField("ФИО пользователя", max_length=128, unique=True)
    phone = models.IntegerField("Номер телефона")
    email = models.EmailField()

    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Account(models.Model):
    """Банковский счёт пользователя"""
    card = models.IntegerField("Номер карты", unique=True)
    date = models.DateTimeField("Дата создания счёта", auto_now_add=True)
    balance = models.DecimalField("Баланс", default=0, max_digits=12, decimal_places=2)
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, to_field="FIO", verbose_name="Пользователь")

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = "Счёт"
        verbose_name_plural = "Счета"


class Master_Account(models.Model):
    """Мастер счёт"""
    balance = models.DecimalField("Баланс", default=0, max_digits=12, decimal_places=2)

    class Meta:
        verbose_name = "Мастер счёт"


class Outlay(models.Model):
    """Списания с карты"""
    date = models.DateTimeField("Дата списания", auto_now_add=True)
    card = models.IntegerField("Номер карты", default=0)
    amount = models.DecimalField("Сумма списания", max_digits=12, decimal_places=2)
    INN = models.IntegerField("ИНН компании")

    def __str__(self):
        return str(self.card)

    class Meta:
        verbose_name = "Списание"
        verbose_name_plural = "Списания"


class Replenishment(models.Model):
    """Пополнение карты"""
    date = models.DateTimeField("Дата пополнения", auto_now_add=True)
    card = models.IntegerField("Номер карты", default=0)
    amount = models.DecimalField("Сумма пополнения", max_digits=12, decimal_places=2)

    def __str__(self):
        return str(self.card)

    class Meta:
        verbose_name = "Пополнение"
        verbose_name_plural = "Пополнения"
