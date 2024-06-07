from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from phones.models import Phone, PhoneInventory

from django.db.models import Sum

def phone_invetory_update():
    phones_count = Phone.objects.all().count()
    phones_value = Phone.objects.aggregate(total_value=Sum('value'))['total_value']
    PhoneInventory.objects.create(phones_count=phones_count, phones_value=phones_value)
    
@receiver(pre_save, sender=Phone)
def phone_pre_save(sender, instance, **kwargs):
    if not instance.bio:
        instance.bio = 'Para mais informações: faleconosco@contato.com'
        
@receiver(post_save, sender=Phone)
def phone_post_save(sender, instance, **kwargs):
    phone_invetory_update()
    
@receiver(post_delete, sender=Phone)
def phone_post_delete(sender, instance, **kwargs):
    phone_invetory_update()