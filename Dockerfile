# Use uma imagem base Python oficial do Docker Hub
FROM python:3.9-slim-buster

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia o arquivo de requirements para o container
COPY requirements.txt .

# Instala as dependências Python
RUN pip install -r requirements.txt

# Copia o código da aplicação para o container
COPY . .

# Expõe a porta 5000 para acesso à aplicação Flask
EXPOSE 5000

# Define o comando para executar a aplicação Flask
CMD ["python", "app.py"]
