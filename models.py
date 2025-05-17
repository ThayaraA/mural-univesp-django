from django.db import models
from django.utils import timezone

class Questao(models.Model):
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    explicacao = models.TextField(blank=True, null=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.titulo
