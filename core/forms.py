from django import forms
from .models import Duvida


class DuvidaForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)


class DuvidaModelForm(forms.ModelForm):
    class Meta:
        model = Duvida
        fields = ['nome', 'email', 'assunto', 'mensagem']
