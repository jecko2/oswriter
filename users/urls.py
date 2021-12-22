from django.urls import path
from . import views

app_name = 'users'
urlpatterns = [
    path('profiles/', views.profile_page, name='profile'),
    path('feedback/', views.send_email, name='feedback'),
    path('feedback/sent/', views.feedback_sent, name='feedback_sent'),
    path('feedback/not-sent/', views.feedback_not_sent, name='feedback_not_sent'),
]

