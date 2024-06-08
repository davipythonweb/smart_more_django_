from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name ='testando'

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)