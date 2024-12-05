from django.test import TestCase
from django.urls import reverse

from .models import Currency

class CurrencyViewTests(TestCase):
    def test_currency_endpoint_returns_all_currencies(self):
        c1 = Currency.objects.create(code="PLN")
        c2 = Currency.objects.create(code="USD")
        c3 = Currency.objects.create(code="EUR")
        expected_endpoint_response = [
            {"code": "PLN"}, {"code": "USD"}, {"code": "EUR"}
        ]
        response = self.client.get(reverse("currency"))
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            expected_endpoint_response    
        )
