from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code


class ExchangeRate(models.Model):
    currency_pair = models.CharField(max_length=6)
    exchange_rate = models.FloatField()

    def __str__(self):
        return f'{self.currency_pair}: {self.exchange_rate}'
