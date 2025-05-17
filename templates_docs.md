# Documentação dos Templates do Sistema de Questões

## Visão Geral

Este documento descreve os templates implementados no sistema de questões, incluindo templates para exibição de questões, explicações e autenticação de usuários.

## Templates de Questões

### 1. Lista de Questões (`lista_questoes.html`)
- **Descrição**: Exibe todas as questões cadastradas no sistema em formato de lista.
- **Funcionalidades**:
  - Listagem de questões ordenadas por data de criação (mais recentes primeiro)
  - Exibição do título, descrição resumida e data de criação
  - Botão para adicionar nova questão

### 2. Detalhes da Questão (`questao_detalhe.html`)
- **Descrição**: Exibe os detalhes completos de uma questão específica.
- **Funcionalidades**:
  - Exibição do título, descrição completa e data de criação
  - Exibição da explicação (quando disponível)
  - Botões para editar e excluir (para usuários autenticados)
  - Layout responsivo com informações adicionais na lateral

### 3. Formulário de Questão (`questao_form.html`)
- **Descrição**: Formulário para adicionar ou editar questões.
- **Funcionalidades**:
  - Campos para título, descrição e explicação
  - Validação de formulário
  - Suporte para criação e edição na mesma interface

### 4. Confirmação de Exclusão (`questao_confirm_delete.html`)
- **Descrição**: Tela de confirmação para exclusão de questões.
- **Funcionalidades**:
  - Confirmação de segurança antes da exclusão
  - Opção para cancelar a operação

## Templates de Autenticação

### 1. Login (`login.html`)
- **Descrição**: Formulário de login para acesso ao sistema.
- **Funcionalidades**:
  - Campos para nome de usuário e senha
  - Link para cadastro de novos usuários
  - Validação de formulário

### 2. Cadastro (`cadastro.html`)
- **Descrição**: Formulário para cadastro de novos usuários.
- **Funcionalidades**:
  - Campos para nome de usuário, senha e confirmação de senha
  - Validação de formulário com mensagens de erro
  - Instruções para criação de senha segura
  - Link para página de login

### 3. Logout (`logout.html`)
- **Descrição**: Página de confirmação de logout.
- **Funcionalidades**:
  - Mensagem de confirmação de saída
  - Link para retornar ao login

## Personalização

Todos os templates utilizam Bootstrap para estilização e são facilmente personalizáveis:

1. Modifique as classes CSS para alterar a aparência
2. Ajuste o layout das páginas conforme necessário
3. Adicione novos elementos HTML mantendo a estrutura básica

## Integração com o Sistema

Os templates estão integrados ao sistema através das views correspondentes:
- `QuestaoListView` para a lista de questões
- `questao_detalhe` para detalhes de questão
- `questao_nova` e `questao_editar` para o formulário
- `questao_excluir` para confirmação de exclusão
- Views de autenticação do Django para login, logout e cadastro
