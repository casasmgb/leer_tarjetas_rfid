from django.db import models

# Create your models here.
class Tarjeta(models.Model):
    uuid = models.CharField(max_length=50, blank=True, default='')
    atr = models.CharField(max_length=50, blank=True, default='')
    created_at = models.DateTimeField(auto_now_add=True)
