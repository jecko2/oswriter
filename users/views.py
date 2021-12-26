from django.shortcuts import render, redirect
from django.core.mail import BadHeaderError, send_mail
from .forms import SendEmailForm
from django.contrib.auth.decorators import login_required


def profile_page(request):
    return render(request, 'users/profile1.html')


@login_required(login_url='account_login')
def send_email(request):
    if request.method == 'GET':
        return render(request, 'users/feedback_form.html')
    if request.method == 'POST':
        form_email = SendEmailForm(request.POST)
        if form_email.is_valid():
            form_user_email = request.user.email
            subject = request.POST.get('subject')
            message = request.POST.get('message')
            print(subject, message)
            if subject and message and form_user_email:
                try:
                    send_mail(subject, message, form_user_email, ['jeckoniaonyango051@gmail.com', ])
                    return redirect('users:feedback_sent')
                except BadHeaderError:
                    return render(request, 'users/feedback_error.html')
        else:
            form_email = SendEmailForm()
        return render(request, 'users/feedback_sent.html')


def feedback_sent(request):
    return render(request, 'users/feedback_sent.html')


def feedback_not_sent(request):
    return render(request, 'users/feedback_error.html')
