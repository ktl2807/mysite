from django.urls import path

from . import views

app_name = 'order'

urlpatterns = [
    path('addOrder/', views.addOrder, name='addOrder'),
]