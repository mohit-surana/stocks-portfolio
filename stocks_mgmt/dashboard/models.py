from django.db import models

class Ticker(models.Model):
    symbol = models.CharField(max_length=8, primary_key=True)
    name = models.CharField(max_length=64)


class Watchlist(models.Model):
    symbol = models.OneToOneField(Ticker, on_delete=models.CASCADE)
    time_added = models.DateTimeField(auto_now=True)


class Portfolio(models.Model):
    symbol = models.OneToOneField(Ticker, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    time_added = models.DateTimeField(auto_now=True)


class HistoricalStockPrice(models.Model):
    symbol = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    date = models.DateField()
    open_price = models.DecimalField(decimal_places=2, max_digits=16)
    close_price = models.DecimalField(decimal_places=2, max_digits=16)
    high = models.DecimalField(decimal_places=2, max_digits=16)
    low = models.DecimalField(decimal_places=2, max_digits=16)
    volume = models.IntegerField()
    time_added = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (
            f'({self.symbol.symbol}, date={self.date}, open={self.open_price}, close={self.close_price}, '
            f'high={self.high}, low={self.low}, volume={self.volume})'
        )

    class Meta:
        unique_together = (('symbol', 'date'),)


class IntradayStockPrice(models.Model):
    symbol = models.ForeignKey(Ticker, on_delete=models.CASCADE)
    time = models.DateTimeField()
    open_price = models.DecimalField(decimal_places=2, max_digits=16)
    close_price = models.DecimalField(decimal_places=2, max_digits=16)
    high = models.DecimalField(decimal_places=2, max_digits=16)
    low = models.DecimalField(decimal_places=2, max_digits=16)
    volume = models.IntegerField()
    time_added = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('symbol', 'time'),)
