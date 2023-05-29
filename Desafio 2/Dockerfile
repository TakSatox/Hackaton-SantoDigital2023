FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

#Criando uma pasta e definindo que tudo será feito nela para melhor organização dos arquivos desta API dentro dos arquivos do container.
WORKDIR /app

#Copia tudo que tem no diretório raiz desse dockerfile e joga no diretorio especificado no workdir que é /app
COPY . .

#Instala tudo que tem no requirements que são justamente as dependências desse projeto
RUN pip install -r requirements.txt

#Expor a porta 8000
EXPOSE 8000

#Rodar o server uvicorn no endereço raiz 0.0.0.0 e especificando porta 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

