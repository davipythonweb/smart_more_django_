from django.contrib import admin
from phones.models import Phone, Model

class ModelAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('release_year', 'model', 'title', 'value')
    search_fields = ('model', 'release_year')
    
admin.site.register(Model, ModelAdmin)
admin.site.register(Phone, PhoneAdmin)