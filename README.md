# Proyecto  – Selenium Docker POC
Automatización de pruebas web usando Selenium desde contenedores Docker.

**Universidad:** Universidad Politécnica Internacional (UPI)  
**Curso:** Organización de Archivos  

## Grupo 3
- Chaves Mora Luis Angel
- Espinoza Alfaro Johan  
- Franceschi Ostty Antonio
- Santamaria Allen Akane

## Estructura del Proyecto

```
selenium-project/
├── Dockerfile                # Imagen Docker para automatización
├── test_script.py            # Script Python con Selenium
├── automate.bat              # Script de automatización completa
└── screenshots/              # Capturas generadas
    └── evidence.png
```

## Cómo Funciona

### Dockerfile
- Imagen base: `python:3.9-slim`
- Instala Selenium 4.15.0
- Configura directorio `/app` y `/app/screenshots`
- Copia y ejecuta `test_script.py`

### test_script.py
- Conecta a contenedor Selenium via `http://selenium-chrome:4444`
- Abre Wikipedia automáticamente
- Busca texto "technology"
- Captura pantalla como `evidence.png`

### Red Docker
- Crea red personalizada `selenium-network`
- Permite comunicación entre contenedores por nombre

## Ejecución

### Comando Completo (Windows)
```bash
docker network create selenium-network && docker run -d --name selenium-chrome --network selenium-network -p 4444:4444 -p 7900:7900 selenium/standalone-chrome:latest && timeout 15 && docker build -f Dockerfile -t selenium-automation . && docker run --rm --name automation-test --network selenium-network -v %cd%/screenshots:/app/screenshots selenium-automation
```
### Script Automatizado (Windows)
```bash
automate.bat
```

## Verificación

### Selenium Hub
```
http://localhost:4444
```

### VNC (Ver navegador en tiempo real)
```
http://localhost:7900
Password: secret
```

### Ver capturas generadas
```bash
dir screenshots        # Windows
ls screenshots/        # Linux/Mac
```

## Personalización

### Cambiar sitio web
En `test_script.py` línea 20:
```python
driver.get("https://www.wikipedia.org")  # Cambiar URL
```

### Cambiar selector de búsqueda
En `test_script.py` línea 26:
```python
search_box = driver.find_element(By.ID, "searchInput")  # Cambiar selector
```

### Cambiar texto a buscar
En `test_script.py` línea 29:
```python
search_text = "technology"  # Cambiar texto
```

### Ejemplos de otros sitios

| Sitio | URL | Selector | 
|-------|-----|----------|
| YouTube | `https://www.youtube.com` | `By.NAME, "search_query"` |
| Google | `https://www.google.com` | `By.NAME, "q"` |
| Amazon | `https://www.amazon.com` | `By.ID, "twotabsearchtextbox"` |

## Limpieza

```bash
docker stop selenium-chrome && docker rm selenium-chrome && docker network rm selenium-network
```

## Requisitos

- Docker Desktop instalado
- Puertos 4444 y 7900 disponibles
- Conexión a internet