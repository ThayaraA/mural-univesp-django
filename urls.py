from django.urls import path
from . import views

app_name = 'mural'

urlpatterns = [
    # Exemplo de rotas para o app mural
    path('', views.mural_home, name='home'),
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:post_id>/', views.post_detail, name='post_detail'),
    path('posts/novo/', views.post_create, name='post_create'),
    path('posts/<int:post_id>/editar/', views.post_edit, name='post_edit'),
    path('posts/<int:post_id>/excluir/', views.post_delete, name='post_delete'),
]
