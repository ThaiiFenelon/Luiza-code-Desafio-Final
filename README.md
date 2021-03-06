# Luiza-code-Desafio-Final

# Objetivo: 
Desenvolver um sistema web para criar um novo registro, exibir informações, atualizar dados e remover registro de produtos de determinadas empresas.

# Requisitos:
- Adicionar empresas;
- Adicionar produtos das empresas cadastradas;
- Remover um produto da empresa; 
- Consultar todos os produtos disponíveis que tal empresa possui; 
- Consultar a lista de empresas cadastradas e trazer os produtos cadastrados.

# Ferramentas de Gestão
- Umense
- Kanba

# Recursos Utilizados no Desenvolvimento da Aplicação:
- BackEnd: 
  MySQL
  Python
  Framework Django
  WampServer (Windows, Apache2, PHP e MySQL)
  VSCode

- FrontEnd:
  Bootstrap
  HTML
  Javascript
  CSS
  VSCode

- Deploy:
  Docker (implementação e virtualização de containers)
  Kurbenetes (sistema de orquestração de containers)

- Versionamento:
  Git
  GitHub

# Executando a aplicação localmente
- Baixar e instalar o WAMP server;
- Acessar o http://localhost/phpmyadmin;
- Ir em Novo, criar banco de dados chamado 'sistema', utf 8 general ci;
- Baixar o arquivo: mysqlclient-1.4.6-cp39-cp39-win_amd64.whl no link >https://www.lfd.uci.edu/~gohlke/pythonlibs/#mysqlclient<
- Rodar o arquivo, a migração das tabelas pro mysql e o localhost do projeto:
  pip install mysqlclient-1.4.6-cp38-cp38-win32.whl
  python manage.py migrate
  python manage.py runserver
- Agora acessa o http://localhost:8000/

# Configuração do Docker em um projeto Django
- Criar o arquivo Dockerfile;
- build a imagem seguindo esse formato de tag: docker build -t nomedorepositório/luiza-code-desafio-final;
- Rodar a imagem docker run -d -p 8000:8000 -it luiza-code-desafio-final;
- No terminal logar no DockerHub: docker login;
- Fazer o build dessa imagem pro DockerHub: docker push nomedorepositório/luiza-code-desafio-final

# Deploy em Kubernetes
- Build Docker
  docker build -t didox/app-luiza-code-desafio-final -f Dockerfile
- Build Docker and run
  docker run -d -p 80:3000 --name app-luiza-code-desafio-final didox/app-luiza-code-desafio-final
- Build watch Docker
  docker run -it -p 80:3000 --name app-luiza-code-desafio-final didox/app-luiza-code-desafio-final
- Para parar o docker
  docker stop app-luiza-code-desafio-final
- Para remover a imagem do docker
  docker rm app-luiza-code-desafio-final
- Para depurar
  docker attach app-luiza-code-desafio-final
- Entra dentro do container
  docker exec -it app-luiza-code-desafio-final bash
- Roda comando dentro do container
  docker exec -it app-luiza-code-desafio-final ls -la
- Para ver logs
  docker logs app-luiza-code-desafio-final -f --tail 100
- Gerar a tag da imagem no docker hub, coloca como latest
  docker tag didox/app-luiza-code-desafio-final hub.docker.com/r/didox/app-luiza-code-desafio-final
- Gerar a tag da imagem no docker hub, com tag 0.0.1
  docker tag didox/app-luiza-code-desafio-final hub.docker.com/r/didox/app-luiza-code-desafio-final:0.0.1
- Publicar a imagem no docker hub, para o latest
  docker push didox/app-luiza-code-desafio-final
- Publicar a imagem no docker hub, para o tag 
  docker push didox/app-luiza-code-desafio-final:0.0.1


# Autoras
