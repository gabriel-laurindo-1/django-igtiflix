<h1 align=center> IGTIFlix </h1>
<p>Projeto desenvolvido durante o módulo de Aplicações Web do Bootcamp Desenvolver Python da IGTI.</p>

---

## Sobre

<p>Esta aplicação apresenta um CRUD completo desenvolvido utilizando o framework Django. Assim, é possível realizar o cadastro, edição e exclusão de séries e gêneros.</p>

---

## Tecnologias utilizadas

- Django
- HTML/CSS
- SQLite

---

## Instalação

<p>Tem certeza de ter a última versão do [python](https://www.python.org/). Assim, para instalar no windowns siga a seguinte sequencia de comandos:</p>

~~~bash
# Instala o pacote para crar o ambiente virtual
$ pip install virtualenv

# Cria o ambiente virtual de desenvolvimento
$ virtualenv showsenv

# Ativação do ambiente virtual
$ showsenv\Scripts\activate

# Instala os necessários ao projeto
$ pip install -r requirements.txt
~~~

---

## Como rodar a aplicação?

<p>Para iniciar o servidor da aplicação do Django, digite os seguintes comandos no terminal:</p>

~~~bash
# Ativação do ambiente virtual (caso não esteja ativado)
$ showsenv\Scripts\activate

# Inicia o servidor da aplicação (necessário estar na raiz do projeto no cmd ao executar o comando)
$ python manage.py runserver
~~~

---

<p align=center>Desenvolvido por Gabriel Laurindo</p>
