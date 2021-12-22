from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('', views.payment_method, name='payment_method'),
    path('payment_process/', views.make_payment, name='make_payment'),
]
