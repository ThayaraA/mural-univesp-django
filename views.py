from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Views de exemplo para o app mural
def mural_home(request):
    return render(request, 'mural/home.html')

def post_list(request):
    # Aqui você adicionaria a lógica para listar posts
    context = {
        'posts': []  # Substituir por consulta real ao banco de dados
    }
    return render(request, 'mural/post_list.html', context)

def post_detail(request, post_id):
    # Aqui você adicionaria a lógica para exibir detalhes de um post
    context = {
        'post': None  # Substituir por consulta real ao banco de dados
    }
    return render(request, 'mural/post_detail.html', context)

@login_required
def post_create(request):
    # Aqui você adicionaria a lógica para criar um novo post
    if request.method == 'POST':
        # Processar o formulário
        messages.success(request, 'Post criado com sucesso!')
        return redirect('mural:post_list')
    return render(request, 'mural/post_form.html')

@login_required
def post_edit(request, post_id):
    # Aqui você adicionaria a lógica para editar um post existente
    if request.method == 'POST':
        # Processar o formulário
        messages.success(request, 'Post atualizado com sucesso!')
        return redirect('mural:post_detail', post_id=post_id)
    context = {
        'post': None  # Substituir por consulta real ao banco de dados
    }
    return render(request, 'mural/post_form.html', context)

@login_required
def post_delete(request, post_id):
    # Aqui você adicionaria a lógica para excluir um post
    if request.method == 'POST':
        # Excluir o post
        messages.success(request, 'Post excluído com sucesso!')
        return redirect('mural:post_list')
    context = {
        'post': None  # Substituir por consulta real ao banco de dados
    }
    return render(request, 'mural/post_confirm_delete.html', context)
