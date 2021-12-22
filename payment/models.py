from django.db import models
from tasks.models import Task


class PaymentMethod(models.Model):
    PAYMENT_OPTIONS = (
        ('PAYPAL', 'paypal'),
        ('CARD', 'card')
    )
    payment_options = models.CharField(max_length=100, choices=PAYMENT_OPTIONS, default='paypal')

