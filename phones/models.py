from django.db import models

class Model(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    model = models.ForeignKey(Model, on_delete=models.PROTECT, related_name='phone_reference')
    camera = models.CharField(max_length=50, blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='phones/', blank=True, null=True)
    box_contents = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.model
    
class PhoneInventory(models.Model):
    iphones_count = models.IntegerField()
    iphones_value = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']
        
    def __str__(self):
        return f'{self.iphones_count} - {self.iphones_value}'