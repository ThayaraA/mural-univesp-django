from django import forms
from .models import Questao

class QuestaoForm(forms.ModelForm):
    class Meta:
        model = Questao
        fields = ['titulo', 'descricao']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        labels = {
            'titulo': 'Título',
            'descricao': 'Descrição',
        }
