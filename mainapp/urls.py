from django.urls import path
from .  import views

app_name='mainapp'
urlpatterns = [
    path('', views.HomeViewPage.as_view(), name='home')
]
