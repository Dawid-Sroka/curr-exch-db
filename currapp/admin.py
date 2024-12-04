from django.contrib import admin

# Register your models here.

from .models import Currency, ExchangeRateAtDate

class ExchangeRateAtDateAdmin(admin.ModelAdmin):
    fields = ["currency_pair"]
    list_filter = ["currency_pair"]

admin.site.register(Currency)
admin.site.register(ExchangeRateAtDate, ExchangeRateAtDateAdmin)