from django.shortcuts import render
from django.http import HttpResponse

from .models import Currency, ExchangeRateAtDate
from .load_data import load_data_from_yf, load_recent_data_from_yf

import json
from datetime import datetime

import yfinance as yf

def fetch(request):
    currs = ["EUR", "USD", "PLN", "JPY"]
    load_recent_data_from_yf(currs)
    return HttpResponse(f'The server fetched data using yfinance about the following currencies: {currs}')

def currency(request):
    output = Currency.objects.all()
    return HttpResponse(json.dumps([{"code" : e.code} for e in output]))

def currency_exchange(request, base_curr, arg_curr):
    target_pairs = ExchangeRateAtDate.objects.filter(currency_pair = base_curr + arg_curr)
    if target_pairs:
        newest = target_pairs.order_by("-date").first().get_value()
    else:
        newest = {}
    return HttpResponse(json.dumps(newest))
