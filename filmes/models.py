from django.db import models
from usuarios.models import Usuario

# Create your models here. 

RATE_CHOICES = [
    (1, 'RUIM'),
    (2, 'MEDIANO'),
    (3, 'BOM'),
    (4, 'MUITO BOM'),
    (5, 'EXCELENTE')
]

class Review(models.Model):
    filme = models.IntegerField()
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    text = models.TextField(max_length=1000, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self
