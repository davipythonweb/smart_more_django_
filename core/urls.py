from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import register_view, login_view, logout_view
from phones.views import PhonesListView, NewPhoneCreateView, PhoneDetailView, PhoneUpdateView, PhoneDeleteView


urlpatterns = [
    path('', PhonesListView.as_view(), name='phones_list'),
    path('admin/', admin.site.urls),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('new_phone/', NewPhoneCreateView.as_view(), name='new_phone'),
    path('phone/<int:pk>', PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/<int:pk>/update', PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/<int:pk>/delete', PhoneDeleteView.as_view(), name='phone_delete'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT) # para configurar uso de armazenar
