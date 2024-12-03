from django.shortcuts import render
from django.http import HttpResponse

from .models import Currency, ExchangeRateAtDate    
import json
from datetime import datetime

import yfinance as yf

def fetch(request):
    pairs = ["EURUSD", "USDJPY", "PLNUSD"]
    for pair in pairs:
        ticker = pair + "=X"

        end_date = datetime.today().date()
        start_date = "2024-11-25"

        data = yf.download(ticker, start=start_date, end=end_date)

        open_dict = data['Open'].dropna().to_dict()[ticker]
        items = open_dict.items()
        open_dict_formatted = {date.strftime('%Y-%m-%d'): rate for date, rate in items}
        for k, v in open_dict_formatted.items():
            e = ExchangeRateAtDate(currency_pair=pair, exchange_rate=v, date=k)
            e.save()
    return HttpResponse("Hello, data has been fetched.")

def currency(request):
    output = Currency.objects.all()
    return HttpResponse(json.dumps([{"code" : e.code} for e in output]))

def currency_exchange(request, base_curr, arg_curr):
    target_pairs = ExchangeRateAtDate.objects.filter(currency_pair = base_curr + arg_curr)
    newest = target_pairs.order_by("date").first()
    return HttpResponse(json.dumps(newest.get_value()))
