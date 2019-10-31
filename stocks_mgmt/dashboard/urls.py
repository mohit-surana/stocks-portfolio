from django.urls import path

from . import views


# TODO: Enhance API design
urlpatterns = [
    path('', views.index, name='index'),
    path('add_ticker/<str:symbol>/<str:name>/', views.add_ticker, name='add_ticker'),
    path('view_historical/<str:symbol>/', views.view_historical, name='view_historical'),
    path('fetch_historical/<str:symbol>/', views.fetch_historical, name='fetch_historical'),
    path('view_intraday/<str:symbol>/', views.view_intraday, name='view_intraday'),
    path('fetch_intraday/<str:symbol>/', views.fetch_intraday, name='fetch_intraday'),
    path('get_quote/<str:symbol>/', views.get_quote, name='get_quote'),  # Always fetch and view quote to keep it fresh
]
