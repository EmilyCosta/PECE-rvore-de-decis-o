# Use uma imagem base do Python
FROM python:3.10-slim

# Defina o diretório de trabalho dentro do container
WORKDIR /app

# Copie o arquivo de requisitos para o diretório de trabalho
COPY requirements.txt .

# Instale as dependências necessárias
RUN pip install --no-cache-dir -r requirements.txt

# Copie o restante dos arquivos do projeto para o diretório de trabalho
COPY . .

# Exponha a porta 8000 para acessar a API
EXPOSE 8000

# Comando para rodar o aplicativo (ajuste conforme necessário)
CMD ["python", "app.py"]
