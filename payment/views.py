from django.shortcuts import redirect, render
from django.conf import settings
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
import logging
from django.contrib import messages
from .forms import PaymentMethodForm
from .models import PaymentMethod
from tasks.models import Task
from django.views.decorators.http import require_POST

logger = logging.getLogger(__name__)


@login_required(login_url='account_login')
def payment_method(request):
    if request.method == 'POST':
        form = PaymentMethodForm(request.POST)
        if form.is_valid():
            context = {'form': form}
            payment_method_select = request.POST.get('payment_options')
            print(payment_method_select)
            if payment_method_select == 'CARD':
                return redirect('payment:make_payment')
            if payment_method_select == 'PAYPAL':
                return redirect('payment:make_payment')
            else:
                messages.success(request, 'Please select one of the payment methods')
                return redirect('payment:payment_method')
    else:
        form = PaymentMethodForm()
    return render(request, 'payment/payment_select.html', {'form': form})


def make_payment(request):
    task = Task.objects.all()
    if task.get() == Task:
        print('passed')
    return render(request, 'payment/payment_form.html')
