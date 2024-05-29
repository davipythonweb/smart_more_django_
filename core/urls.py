from django.contrib import admin
from django.urls import path
from django.http import HttpResponse


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda mensagem_teste: HttpResponse(
        '<center><h1>Smart-More|Iphones</h1><center><br> <center><p>Welcome!</p></center>'
    ))
]
