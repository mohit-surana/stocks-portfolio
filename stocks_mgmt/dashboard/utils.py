import datetime
import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import re
from dateutil.relativedelta import relativedelta

from .models import HistoricalStockPrice, IntradayStockPrice


def get_relative_delta(duration):
    num, unit = re.match('(\d+)([ymwd])', duration).groups()
    num = int(num)

    if unit == 'y':
        return relativedelta(years=num)
    elif unit == 'm':
        return relativedelta(months=num)
    elif unit == 'w':
        return relativedelta(weeks=num)
    elif unit == 'd':
        return relativedelta(days=num)

def queryset_to_df(queryset):
    df = pd.DataFrame.from_records(queryset.values())
    return df

def plot_chart(symbol, duration):
    pio.renderers.default = 'browser'

    delta = get_relative_delta(duration)
    two_weeks_delta = get_relative_delta('2w')
    min_timestamp = datetime.datetime.now() - delta
    two_weeks_ago = datetime.datetime.now() - two_weeks_delta

    if min_timestamp < two_weeks_ago:
        time_col = 'date'
        stock_price = HistoricalStockPrice.objects.filter(
        symbol=symbol,
        date__gt=min_timestamp
    )
    else:
        time_col = 'time'
        stock_price = IntradayStockPrice.objects.filter(
        symbol=symbol,
        time__gt=min_timestamp
    )

    stock_price_df = queryset_to_df(stock_price)
    fig = go.Figure(data=[go.Candlestick(x=stock_price_df[time_col],
                                         open=stock_price_df['open_price'],
                                         high=stock_price_df['high'],
                                         low=stock_price_df['low'],
                                         close=stock_price_df['close_price'])])

    fig.update_layout(title=f'{symbol} Stock Price')
    fig.show()