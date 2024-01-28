from django.urls import path

from moex_client import views

urlpatterns = [
    path('get-current-usd/', views.get_current_usd),
]
