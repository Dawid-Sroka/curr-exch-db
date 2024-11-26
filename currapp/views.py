from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def currency(request):
    return HttpResponse("currency endpoint")

def currency_exchange(request, base_curr, arg_curr):
    return HttpResponse(f"currency exchange of {base_curr} to {arg_curr} endpoint")
