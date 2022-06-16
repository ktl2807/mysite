from audioop import add
from django.urls import path
from.import views

app_name='basket'

urlpatterns = [
    path('', views.basket_summary, name='basket_summary'),
    path('add/', views.basket_add, name='basket_add'),
    path('change/', views.basket_change, name='basket_change'),
]
