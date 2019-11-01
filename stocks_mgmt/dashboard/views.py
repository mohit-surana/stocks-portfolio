from django.http import HttpResponse
from django.shortcuts import render

from .models import HistoricalStockPrice, IntradayStockPrice, Quote, Ticker
from .external_calls import fetch_historical_price, fetch_intraday_price, fetch_quote
from .utils import plot_chart

def index(request):
    return HttpResponse('Moon lambo is not too far away!')

# TODO: Possibly prefetch all symbols?
def add_ticker(request, symbol, name):
    ticker = Ticker(symbol=symbol, name=name)
    ticker.save()
    return HttpResponse(f'Added {name} ({symbol}) to list of symbols!')

def view_historical(request, symbol):
    historical_price = HistoricalStockPrice.objects.filter(symbol=symbol)
    if historical_price:
        return HttpResponse(historical_price)
    else:
        return HttpResponse(f'Please fetch the historical stock price for {symbol=}!')

# TODO: Improve error handling
def fetch_historical(request, symbol):
    fetch_historical_price(symbol)
    return HttpResponse(f'Fetched the historical stock price for {symbol=}!')

def view_intraday(request, symbol):
    intraday_price = IntradayStockPrice.objects.filter(symbol=symbol)
    if intraday_price:
        return HttpResponse(intraday_price)
    else:
        return HttpResponse(f'Please fetch the intraday stock price for {symbol=}!')

# TODO: Improve error handling
def fetch_intraday(request, symbol):
    fetch_intraday_price(symbol)
    return HttpResponse(f'Fetched the intraday stock price for {symbol=}!')

# TODO: Improve error handling
def get_quote(request, symbol):
    quote = fetch_quote(symbol)
    return HttpResponse(quote)

def visualization(request, symbol):
    plot_chart(symbol, duration='1y')
    return HttpResponse('Check out the other browser tab!')
