from tkinter.font import names

from django.urls import path

from .views import index, professor, aluno

urlpatterns = [
    path('', index, name='index'),
    path('professor', professor, name='professor'),
    path('aluno', aluno, name='aluno'),
]
