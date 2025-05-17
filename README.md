# Sistema de Questões

Um sistema web desenvolvido em Django para gerenciar questões, com funcionalidades de autenticação e formulários.

## Funcionalidades

- Listagem de questões
- Autenticação (login, logout, cadastro)
- Adição de novas questões via formulário

## Requisitos

- Python 3.8+
- Django 5.2+

## Instalação

1. Clone o repositório:
```
git clone https://github.com/seu-usuario/questoes_app.git
cd questoes_app
```

2. Instale as dependências:
```
pip install django
```

3. Execute as migrações:
```
python manage.py migrate
```

4. Inicie o servidor:
```
python manage.py runserver
```

5. Acesse a aplicação em `http://localhost:8000`

## Estrutura do Projeto

- `questoes/` - Aplicativo principal
  - `models.py` - Modelo de dados para questões
  - `views.py` - Views para listar questões e autenticação
  - `forms.py` - Formulários para adicionar questões
  - `templates/` - Templates HTML
- `questoes_app/` - Configurações do projeto Django

## Como Usar

1. Cadastre-se no sistema
2. Faça login com suas credenciais
3. Visualize a lista de questões
4. Adicione novas questões através do formulário
