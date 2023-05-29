<h1 align="center">:file_cabinet: Desafio2 - Hackaton Santo Digital 2023</h1>

## :memo: Descrição
Nesse projeto, aproveitando o banco de dados contido no container que foi criado a partir do desafio 1, foram criados endpoints para realizar CRUD na tabela products e também com rotas específicas para obter os 10 produtos mais vendidos por categoria, cliente com maior número de pedidos, mês com maior quantidade de vendas em valor total e regiões com vendas acima da média.

Rotas que podem ser utilizadas:

* http://127.0.0.1:8000/products -> Get em todos os produtos ou Post.
* http://127.0.0.1:8000/products/{id} -> Get em um produto específico, Put ou Delete.
* http://127.0.0.1:8000/sales/top-products/{category} -> Top 10 produtos na categoria específica.
* http://127.0.0.1:8000/sales/sales/best-customer -> Cliente com maior número de pedidos.
* http://127.0.0.1:8000/busiest_month -> Mês com maior valor total de vendas.
* http://127.0.0.1:8000/top-region-sellers -> Regiões com quantidade de vendas acima da média.


## :wrench: Tecnologias utilizadas
* VScode
* Docker
* SQLAlchemy
* Pydantic
* Starlette
* Python Built-in: calendar

## :rocket: Rodando o projeto
Para utilizar este projeto, é necessário ter o banco de dados criado no desafio 1 e configurar o arquivo database.py para adequar-se ao banco de dados. A partir daqui há dois caminhos: utilizando ou não container do docker. 

Não utilizando, basta rodar o comando uvicorn app:main que já será possível realizar as requisições.

Utilizando, será necessário criar primeiro a imagem com docker "build -t nomeimagem ." e em seguida criar o container com "docker run -d -p 8000:8000 nomeimagem". Na configuração do database.py é importante colocar no host o valor "host.docker.internal" para que a API no container possa encontrar o endereço local do localhost e dessa forma permitir requisições.