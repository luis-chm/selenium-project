# Dockerfile para automatizar ejecución de Selenium
FROM python:3.9-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y wget curl && rm -rf /var/lib/apt/lists/*

# Instalar Selenium
RUN pip install selenium==4.15.0

# Crear directorio de trabajo
WORKDIR /app

# Crear directorio para capturas
RUN mkdir -p /app/screenshots

# Copiar script automatizado
COPY test_script.py .

# Punto de entrada automatizado
CMD ["python", "test_script.py"]