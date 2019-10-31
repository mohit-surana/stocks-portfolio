from django.urls import path

from . import views


# TODO: Enhance API design
urlpatterns = [
    path('', views.index, name='index'),
    path('add_ticker/<str:symbol>/<str:name>/', views.add_ticker, name='add_ticker'),
    path('view_historical/<str:symbol>/', views.view_historical, name='view_historical'),
    path('fetch_historical/<str:symbol>/', views.fetch_historical, name='fetch_historical'),
]

