# 🛒 Loja Virtual Python (Django)

Projeto final desenvolvido para a U.C. 3 do curso de Python. O sistema consiste em uma loja virtual completa com funcionalidades de CRUD, autenticação de usuários e carrinho de compras baseados em sessão.

## 📋 Funcionalidades

* *Área Pública:* Vitrine de produtos, busca/filtro, detalhe do produto.
* *Área do Usuário:* Cadastro, Login, Logout, Carrinho de Compras (Sessão).
* *Área Administrativa:* Gestão de Produtos (CRUD) e Categorias com upload de imagens.

## 🛠 Tecnologias Utilizadas

* Python 3.x
* Django 5.x
* Bootstrap 5 (Front-end)
* SQLite (Banco de Dados)

## 🚀 Como Executar o Projeto

1.  *Clone o repositório:*
    bash
    git clone <link-do-seu-repositorio-aqui>
    cd projeto_final_python
    
2.  *Crie e ative o ambiente virtual:*
    bash
    # Windows
    python -m venv venv
    venv\Scripts\activate
    
    # Linux/Mac
    python3 -m venv venv
    source venv/bin/activate
    
3.  *Instale as dependências:*
    bash
    pip install -r requirements.txt
    
4.  *Aplique as migrações ao banco de dados:*
    bash
    python manage.py migrate
    
5.  *Crie um superusuário (para acessar o painel admin):*
    bash
    python manage.py createsuperuser
    
6.  *Inicie o servidor:*
    bash
    python manage.py runserver
    
7.  *Acesse no navegador:*
    * Loja: http://127.0.0.1:8000/
    * Admin: http://127.0.0.1:8000/admin