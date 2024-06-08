from django.urls import path
from .views import phones
from django.conf import settings
from django.conf.urls.static import static


urlpatters = [
    path('', phones, name='phones_list'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)