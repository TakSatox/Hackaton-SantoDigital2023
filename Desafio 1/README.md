<h1 align="center">:file_cabinet: Desafio1 - Hackaton Santo Digital 2023</h1>

## :memo: Descrição
Nesse projeto, tendo como base o dataset em https://www.kaggle.com/datasets/ukveteran/adventure-works, foi criado um banco de dados fictício contendo tabelas e dados referentes vendas realizadas, clientes, produtos, categorias e subcategorias de produtos, territórios, entre outros. Com as tabelas criadas, foram inseridos nelas os dados contidos nos arquivos csv também fornecidos no dataset.
Após a inserção, foram realizadas queries para filtrar os dados em:  "10 produtos mais vendidos na categoria bicicleta", "Cliente com maior número de pedidos realizados", "Mês do ano que ocorrem mais vendas em valor total", "Regiões com vendas acima da média" (que foi na realidade uma adaptação mais próxima do solicitado "vendedores com vendas acima da média" visto que não há a tabela de vendedores no dataset) e "Os 20 clientes com menor quantidade de pedidos" (Para fins de marketing direcionado). Ainda na filtragem de dados, os dados retornados de cada query foram exportados como csv na pasta csvexports. Por último foi criado um Dockerfile para criar uma imagem do banco de dados e a partir dela criar containers no Docker.

## :wrench: Tecnologias utilizadas
VScode
Docker
SQLAlchemy
Pandas
Python Built-in: calendar

## :rocket: Rodando o projeto
Para utilizar este projeto, é necessário primeiramente instalar o banco de dados MySQL ou apenas o Docker e configurar os valores em config do arquivo database.py para que a conexão seja feita corretamente. No caso do MySQL, basta apenas configurar o User e Password, colocando os mesmos da conexão que possuir no MySQL. No caso do docker, primeiro deve construir a imagem com "docker build -t nomeimagem ." sem as aspas, em seguida criar o container com "docker run -d -P nomeimagem". Após isso ir no Docker Desktop para verificar a porta que foi definida na inicialização do container e inserir ela alterando o dicionário config de database.py.
Feito essas configurações iniciais, basta executar os arquivos na ordem: main.py (para que sejam criadas as tabelas), importcsv.py (para que os inserts sejam realizados na tabela), queries.py (para que os dados filtrados sejam exportados em csv).
