from django.urls import path

from . import views

urlpatterns = [
    path("fetch", views.fetch, name="fetching"),
    path("", views.currency, name="currency"),
    path("<str:base_curr>/<str:arg_curr>/", views.currency_exchange, name="currency_exchange"),
]