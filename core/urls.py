from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('tasks/', include('tasks.urls', namespace='task')),
    path('accounts/', include('allauth.urls')),
    path('payments/', include('payment.urls', namespace='payment')),
    path('', include('mainapp.urls', namespace='mainapp'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
