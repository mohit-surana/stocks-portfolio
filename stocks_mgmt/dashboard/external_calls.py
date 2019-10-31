import requests

from django.conf import settings
from django.db import transaction

from .models import HistoricalStockPrice, IntradayStockPrice, Ticker


def alphavantage_request(function, **query_params):
    query_params.update({
        'function': function,
        'apikey': settings.ALPHAVANTAGE_API_KEY,
    })
    return requests.get(
        settings.ALPHAVANTAGE_QUERY_URL,
        params=query_params
    )

@transaction.atomic
def fetch_historical_price(symbol, outputsize='full'):
    # TODO: Dynamically infer outputsize by looking at the last fetched recoord in the database
    ticker_object = Ticker.objects.filter(symbol=symbol).first()
    if ticker_object:
        response = alphavantage_request(
            function='TIME_SERIES_DAILY',
            symbol=symbol,
            outputsize=outputsize
        )
        result = response.json()
        for date, data in result['Time Series (Daily)'].items():
            hsp_obj, created = HistoricalStockPrice.objects.update_or_create(
                defaults={
                    'symbol': ticker_object,
                    'date': date,
                    'open_price': data['1. open'],
                    'close_price': data['4. close'],
                    'high': data['2. high'],
                    'low': data['3. low'],
                    'volume': data['5. volume'],
                },
                symbol=ticker_object,
                date=date,
            )
    else:
        raise Exception(f'Add ticker {symbol=} to the database first!')

@transaction.atomic
def fetch_intraday_price(symbol, outputsize='full', interval='5min'):
    # TODO: Dynamically infer outputsize by looking at the last fetched record in the database
    ticker_object = Ticker.objects.filter(symbol=symbol).first()
    if ticker_object:
        response = alphavantage_request(
            function='TIME_SERIES_INTRADAY',
            symbol=symbol,
            outputsize=outputsize,
            interval=interval,
        )
        result = response.json()
        for time, data in result[f'Time Series ({interval})'].items():
            isp_obj, created = IntradayStockPrice.objects.update_or_create(
                defaults={
                    'symbol': ticker_object,
                    'time': time,
                    'open_price': data['1. open'],
                    'close_price': data['4. close'],
                    'high': data['2. high'],
                    'low': data['3. low'],
                    'volume': data['5. volume'],
                },
                symbol=ticker_object,
                time=time,
            )
    else:
        raise Exception(f'Add ticker {symbol=} to the database first!')
