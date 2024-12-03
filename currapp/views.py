from django.shortcuts import render
from django.http import HttpResponse

from .models import Currency, ExchangeRateAtDate    
import json

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def currency(request):
    output = Currency.objects.all()
    return HttpResponse(json.dumps([{"code" : e.code} for e in output]))

def currency_exchange(request, base_curr, arg_curr):
    target_pairs = ExchangeRateAtDate.objects.filter(currency_pair = base_curr + arg_curr)
    newest = target_pairs.order_by("date")[0]
    return HttpResponse(json.dumps(newest.get_value()))
