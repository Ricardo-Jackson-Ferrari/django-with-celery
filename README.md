<p align="center">
  <a href="https://www.djangoproject.com" target="blank"><img src="https://code.djangoproject.com/raw-attachment/ticket/24953/django-hexbin.png" width="200" alt="Django Logo" /></a>
</p>

<p align="center">
  <a href="#-tecnologias">Tecnologias</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-projeto">Projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#-como-executar">Como executar</a>
</p>


<hr>

<a id="-tecnologias"></a>

## Tecnologias

Esse projeto foi desenvolvido com a seguinte tecnologia:

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?&style=for-the-badge&logo=redis&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)


<hr>

<a id="-projeto"></a>

## 💻 Projeto

O projeto Django-With-Celery foi desenvolvido como um exemplo de implementação de uma aplicação web com Django e sistema de mensageria. O acesso padrão do Django foi alterado de username para email, aonde a conta recém criada se encontra inativa e um email de ativação é enviado.

<p align="center">
  <img alt="Página inicial" src=".github/media/home.jpg" width="100%">
</p>

<p align="center">
  <img alt="Registro" src=".github/media/registro.jpg" width="100%">
</p>

<p align="center">
  <img alt="Lista de tasks" src=".github/media/listagem_tasks.jpg" width="100%">
</p>

<p align="center">
  <img alt="Task com url de ativação" src=".github/media/task_com_url_ativacao.jpg" width="100%">
</p>

<p align="center">
  <img alt="Página login" src=".github/media/login.jpg" width="100%">
</p>

<p align="center">
  <img alt="Acesso usuário não ativo" src=".github/media/acesso_usuario_nao_ativo.jpg" width="100%">
</p>

<p align="center">
  <img alt="Ativação usuário" src=".github/media/ativacao_usuario.jpg" width="100%">
</p>

<p align="center">
  <img alt="Acesso realizado" src=".github/media/acesso_realizado.jpg" width="100%">
</p>

<a id="-como-executar"></a>

## 🚀 Como executar

### 💻 Pré-requisitos
 **Antes de começar, verifique se você atendeu aos seguintes requisitos:**

- Você tem uma máquina `< Windows / Linux / Mac >`.

- Você instalou a versão mais recente de `< Docker >`


### Como instalar localmente:

- clone ou baixe o repositório.

Com o ambiente virtual ativo:

- Altere o arquivo `env` com as informações que desejar e depois renomeie para `.env`.

## 🚁 Pequena ajuda
O projeto conta com um arquivo Makefile para facilitar os comandos.

## 👨‍💻 Ativando a aplicação
Para executar a aplicação(Com o Docker ativo):

- Acesse a pasta do projeto no terminal e execute:

```console
docker-compose up -d --build -V
```

Após o código finalizar a execução você poderá acessar a aplicação em [localhost:8000](localhost:8000) no seu navegador.

Obs: Para acessar o painel admistrativo da aplicação é necessário criar um superusuário.

- Com a aplicação em execução acesse o terminal e execute:

```console
docker-compose exec app python manage.py createsuperuser
```

Após a criação do superusuário você poderá acessar o painel administrativo da aplicação em [localhost:8000/admin](localhost:8000/admin) no seu navegador.

## 👨‍💻 Parando a aplicação
- Acesse a pasta do projeto no terminal e execute:

```console
docker-compose down
```