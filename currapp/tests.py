from django.test import TestCase
from django.urls import reverse

from .models import Currency, ExchangeRateAtDate
from .load_data import load_data_from_yf

class CurrencyViewTests(TestCase):
    def test_currency_returns_three_currencies(self):
        c1 = Currency.objects.create(code="PLN")
        c2 = Currency.objects.create(code="USD")
        c3 = Currency.objects.create(code="EUR")
        expected_currencies_list = [
            {"code": "PLN"}, {"code": "USD"}, {"code": "EUR"}
        ]
        response = self.client.get(reverse("currency"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            expected_currencies_list    
        )

    def test_currency_returns_empty_list_when_database_empty(self):
        response = self.client.get(reverse("currency"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            []    
        )


class CurrencyExchangeViewTests(TestCase):
    def test_currency_exchange_returns_correct_value(self):
        print() # just because fetching from yf overrides test name in terminal
        load_data_from_yf(["PLN", "USD"], "2024-12-02", "2024-12-05")
        expected_exchange_rate = {"currency_pair": "USDPLN", "exchange_rate": 4.083}
        response = self.client.get(reverse("currency_exchange", args=['USD', 'PLN']))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            expected_exchange_rate    
        )

    def test_currency_exchange_returns_empty_dict_when_currency_not_in_db(self):
        response = self.client.get(reverse("currency_exchange", args=['USD', 'PLN']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            str(response.content, encoding='utf8'),
            "Sorry, this currency pair is not present in the database"
        )