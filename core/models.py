from django.db import models
from stdimage.models import StdImageField
from django.db.models import signals
from django.template.defaultfilters import slugify

class Base(models.Model):
    criado = models.DateField('Data de Criação', auto_now_add=True)
    modificado = models.DateField('Data de Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract=True


class Duvida(Base):
    nome = models.CharField('Nome', max_length=100)
    email = models.DecimalField('Email', max_digits=8, decimal_places=2)
    mensagem = models.CharField('Mensagem', max_length=100)
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)
    def __str__(self):
        return self.nome

def duvida_pre_save(signal, instance, sender, **kwargs):
    instance.slug = slugify(instance.nome)

signals.pre_save.connect(duvida_pre_save, sender=Duvida)