# smart_more_django_

`ecommerce_de_smartphones_apple`

- migrando para banco PostgreSQL
`comandos`
`acessar shell postgres (windows)`
- psql -U postgres
`lista todos os bancos`
- \l
`criar banco`
- CREATE DATABASE (nome do banco);
`sair`
- \q
`drive para django e postgres`
- pip install psycopg2
`para usar variaveis de ambient`
- pip install python-dotenv

## comandos django

- criado projeto
  django-admin startproject core .
- rodar projeto
  python manage.py runserver
- criando app
  python manage.py startapp + nome
- criar as tabelas no banco
  python manage.py migrate
- fazendo mudancas e criar os arquivos de migracoes
  python manage.py makemigrations
- criando super usuario admin
  python manage.py createsuperuser user>admin
- instalar pacote
  pip install + nome do pacote
- fazer os testes
  python manage.py test

### Django Shell

`python manage.py shell`  

#### ACESSO-SGBD

- USER  CONFIG => `root`
- EMAIL CONFIG => `root@master.com`
- PASS CONFIG => `Root$acesso5`

- NOVO USUARIO PARA TESTE: `teste_user`
- PASS USUARIO TESTE: `Teste@123`

##### pytest

`pip install pytest pytest-django`

##### usage

-runing pytest- rodar no terminal => pytest

- para ver tudo => pytest -rP

- runing unitest- para o test_django => python manage.py test