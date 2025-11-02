# MyTaskApp - Backend

API REST para gerenciamento de tarefas (To-Do) com Django 4.x, Django REST Framework, Djoser e JWT.
Cada tarefa é associada a um usuário, garantindo isolamento de dados.

## Funcionalidades

Cadastro e login de usuários via JWT (Djoser + SimpleJWT)

CRUD completo de tarefas

Marcação de tarefas como concluídas

Filtros por status (pendente/concluída) e tipo

Ordenação por data de criação

Cada usuário vê apenas suas próprias tarefas

Validações de campos (título, descrição e tipo obrigatórios)

Mensagens de erro claras para debugging

## Tecnologias Utilizadas

Backend: Django, Django REST Framework, Djoser

Autenticação: JWT (djangorestframework-simplejwt)

Filtros e Ordenação: django-filter

Banco de Dados: SQLite (desenvolvimento), compatível com PostgreSQL

## Instalação e Execução

Clone o repositório

Crie e ative o ambiente virtual

Windows:
python -m venv venv
venv\Scripts\activate

Linux/macOS:
python3 -m venv venv
source venv/bin/activate

Instale as dependências
pip install -r requirements.txt

Configure variáveis de ambiente
Crie um arquivo .env baseado no .env.example.

Exemplo:
SECRET_KEY=sua_chave_secreta
DEBUG=True
ALLOWED_HOSTS=127.0.0.1,localhost

Rode as migrações do banco
python manage.py makemigrations
python manage.py migrate

Crie um superusuário (opcional, para acessar o admin)
python manage.py createsuperuser

Inicie o servidor de desenvolvimento
python manage.py runserver 0.0.0.0:8000

O backend estará disponível no IP local da sua máquina.

## Endpoints Principais
Autenticação (Djoser + SimpleJWT)

Rota | Método | Descrição | Requisição | Resposta
/auth/users/ | POST | Cadastro de usuário | username, password, email (opcional) | Dados do usuário cadastrado
/auth/jwt/create/ | POST | Login (obter tokens) | username, password | access e refresh tokens JWT
/auth/jwt/refresh/ | POST | Atualizar access token | refresh token | Novo access token
/auth/jwt/verify/ | POST | Verificar validade do token | token | OK ou erro

Tarefas

Rota | Método | Descrição | Requisição | Resposta
/tarefas/ | GET | Listar tarefas do usuário | Header Authorization + filtros opcionais | Lista de tarefas
/tarefas/ | POST | Criar nova tarefa | Header Authorization + dados da tarefa | Dados da tarefa criada
/tarefas/{id}/ | GET | Detalhar tarefa | Header Authorization | Dados da tarefa
/tarefas/{id}/ | PUT | Atualizar tarefa | Header Authorization + dados atualizados | Dados atualizados
/tarefas/{id}/ | PATCH | Atualizar parcialmente | Header Authorization + dados parciais | Dados atualizados
/tarefas/{id}/ | DELETE | Deletar tarefa | Header Authorization | HTTP 204 No Content

## Observações 

Header Authorization é obrigatório nas rotas protegidas:
Authorization: Bearer <access_token>

O campo “usuario” é atribuído automaticamente pelo backend e não deve ser enviado.

Filtros e ordenação via query params:
Exemplo: /tarefas/?status=False&ordering=-dataCriacao

## Testes
python manage.py test

## Autor
Lucas Tamborim — GitHub

## Licença
MIT License
