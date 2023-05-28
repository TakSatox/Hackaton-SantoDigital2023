# Criando a imagem para que a partir dela seja possível criar containers no Docker

# Utilizando a versão mais recente do mysql
FROM mysql:latest

#Definindo variáveis na inicialização
ENV MYSQL_ROOT_PASSWORD=1234
ENV MYSQL_DATABASE=adventureworks
#Para que não seja negado o acesso ao servidor, foi necessário utilizar este artifício
ENV MYSQL_ROOT_HOST='%'

COPY script.sql /docker-entrypoint-initdb.d/
