from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return self.code


class ExchangeRateAtDate(models.Model):
    currency_pair = models.CharField(max_length=6)
    exchange_rate = models.FloatField()
    date = models.DateTimeField("date registered")

    def get_value(self):
        return {"currency_pair": self.currency_pair, "exchange_rate": f'{self.exchange_rate:.3f}'}

    def __str__(self):
        return f'{self.currency_pair}: {self.exchange_rate:.3f} at {self.date}' 
