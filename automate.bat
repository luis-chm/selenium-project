@echo off
echo INICIANDO AUTOMATIZACIÓN TOTAL

REM Limpiar ambiente anterior
docker stop selenium-chrome >nul 2>&1
docker rm selenium-chrome >nul 2>&1
docker network rm selenium-net >nul 2>&1

REM Crear infraestructura automatizada
echo Creando red automatizada...
docker network create selenium-net

echo Iniciando Selenium automatizado...
docker run -d --name selenium-chrome --network selenium-net -p 4444:4444 -p 7900:7900 selenium/standalone-chrome:latest

echo Esperando que Selenium esté listo...
timeout 15

echo Construyendo imagen automatizada...
docker build -f Dockerfile -t selenium-automated .

echo EJECUTANDO AUTOMATIZACIÓN...
docker run --rm --name automated-test --network selenium-net -v %cd%/screenshots:/app/screenshots selenium-automated

echo AUTOMATIZACIÓN COMPLETADA
echo Revisar capturas en: ./screenshots/