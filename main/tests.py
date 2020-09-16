from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Account, Master_Account


class CustomerTests(APITestCase):
    def setUp(self):
        """
        Создаём пользователя и его аккаунт
        """
        Customer.objects.create(id=1, FIO="Иванов И И", phone=34568765, email="ivan@gmail.com")
        Account.objects.create(card=234, balance=100.00, customer=Customer.objects.get(FIO="Иванов И И"))
        Master_Account.objects.create(balance=1000)

    def test_create_customer_and_account(self):
        """
        Создаем экземпляр модели Customer и Account через POST запрос
        """
        url = reverse('customer-list')
        data = {
            "id": 2,
            "FIO": "Петров И И",
            "phone": 24568765,
            "email": "petr@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Customer.objects.count(), 2)
        self.assertEqual(Customer.objects.get(id=2).FIO, 'Петров И И')

        url = reverse('account-list')
        data = {
            "card": 1234,
            "balance": 0.00,
            "customer": "Петров И И"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 2)
        self.assertEqual(Account.objects.get(customer="Петров И И").card, 1234)

    def test_get_balance(self):
        response = self.client.get(reverse('balance'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_balance(self):
        """
        Проверяем баланс
        """
        url = reverse('balance')
        data = {"card": 234}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, 100.00)

    def test_get_replenishment(self):
        response = self.client.get(reverse('replenishment'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_replenishment(self):
        """
        Проводим зачисление
        """
        url = reverse('replenishment')
        data = {"card": 234, "amount": 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.get().balance, 200)
        self.assertEqual(Master_Account.objects.get().balance, 900)

    def test_get_outlay(self):
        response = self.client.get(reverse('outlay'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_outlay(self):
        """
        Проводим списание
        """
        url = reverse('outlay')
        data = {"card": 234, "amount": 100.00, "INN": 54321}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Account.objects.get().balance, 0)
