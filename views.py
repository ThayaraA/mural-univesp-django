from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from .models import Questao
from .forms import QuestaoForm
from django.contrib.auth.forms import UserCreationForm

# View baseada em classe para listar questões
class QuestaoListView(ListView):
    model = Questao
    template_name = 'questoes/lista_questoes.html'
    context_object_name = 'questoes'
    ordering = ['-data_criacao']  # Ordena do mais recente para o mais antigo

# View baseada em função para listar questões (alternativa)
def lista_questoes(request):
    questoes = Questao.objects.all().order_by('-data_criacao')
    return render(request, 'questoes/lista_questoes.html', {'questoes': questoes})

# View para cadastro de usuários
def cadastro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criada para {username}! Agora você pode fazer login.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'questoes/cadastro.html', {'form': form})

# View para adicionar novas questões
@login_required
def questao_nova(request):
    if request.method == 'POST':
        form = QuestaoForm(request.POST)
        if form.is_valid():
            questao = form.save(commit=False)
            questao.save()
            messages.success(request, 'Questão adicionada com sucesso!')
            return redirect('lista_questoes')
    else:
        form = QuestaoForm()
    return render(request, 'questoes/questao_form.html', {'form': form, 'titulo': 'Nova Questão'})
