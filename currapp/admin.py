from django.contrib import admin

# Register your models here.

from .models import Currency, ExchangeRateAtDate

admin.site.register(Currency)
admin.site.register(ExchangeRateAtDate)