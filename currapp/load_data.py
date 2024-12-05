from currapp.models import Currency, ExchangeRateAtDate

import json
from datetime import datetime

import yfinance as yf

def load_recent_data_from_yf(currs):
    start_date = "2024-12-02"
    end_date = datetime.today().date()
    load_data_from_yf(currs, start_date, end_date)

def load_data_from_yf(currs, start_date, end_date):
    for curr in currs:
        c = Currency(code=curr)
        c.save()
    pairs = [c1+c2 for c1 in currs for c2 in currs if c1 != c2]
    for pair in pairs:
        ticker = pair + "=X"

        end_date = datetime.today().date()
        start_date = "2024-12-02"

        yf_data = yf.download(ticker, start=start_date, end=end_date)

        data = yf_data['Open'].dropna().to_dict()[ticker].items()
        open_dict_formatted = {date.strftime('%Y-%m-%d'): rate for date, rate in data}
        for k, v in open_dict_formatted.items():
            _ = ExchangeRateAtDate.objects.get_or_create(currency_pair=pair, exchange_rate=v, date=k)
