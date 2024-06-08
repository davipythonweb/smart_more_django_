from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'namespace'

urlpatterns = [
    path('', views.PhonesListView.as_view(), name='list'),
    path('new_phone/', views.NewPhoneCreateView.as_view(), name='new'),
    path('phone/<int:pk>', views.PhoneDetailView.as_view(), name='detail'),
    path('phone/<int:pk>/update', views.PhoneUpdateView.as_view(), name='update'),
    path('phone/<int:pk>/delete', views.PhoneDeleteView.as_view(), name='delete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)