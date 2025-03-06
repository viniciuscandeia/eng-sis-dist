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

stage('Deploy para Produção') {
      steps {
        echo 'Implantando para Ambiente de Produção...'
        script {
          dockerContainerNameProd = "flask-app-devops-container-prod"
          dockerContainerNameTest = "flask-app-devops-container-test"

          // Para o container de teste (se estiver rodando)
          sh "docker stop ${dockerContainerNameTest} || true"
          sh "docker rm ${dockerContainerNameTest} || true"
            // Para o container de produção existente (se estiver rodando)
          sh "docker stop ${dockerContainerNameProd} || true"
          sh "docker rm ${dockerContainerNameProd} || true"
          // Roda um novo container de produção
          dockerImage.run("--name ${dockerContainerNameProd} -d -p 5000:5000")

          echo "Aplicação implantada em http://localhost:5000 (Produção)"
        }
      }
    }