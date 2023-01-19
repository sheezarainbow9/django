from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
from django.db import models
from django.contrib.auth import get_user_model
class Pessoa(models.Model):
    
    nome = models.CharField(max_length=255)
    telefone = models.IntegerField()
    email = models.EmailField()
    data_nasc = models.DateField(null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

def __str__(self):
    return self.nome