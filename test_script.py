from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import sys

def setup_driver():
    """Configurar Chrome driver para automatización"""
    print("Configurando driver automatizado...")
    
    chrome_options = Options()
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-gpu")
    
    try:
        driver = webdriver.Remote(
            command_executor='http://selenium-chrome:4444/wd/hub',
            options=chrome_options
        )
        print("Driver automatizado configurado correctamente")
        return driver
    except Exception as e:
        print(f"Error en configuracion automatizada: {e}")
        return None

def automated_web_test():
    """AUTOMATIZACIÓN: Abrir web, buscar texto y capturar pantalla"""
    print("INICIANDO AUTOMATIZACION COMPLETA")
    
    driver = setup_driver()
    if not driver:
        return False
    
    try:
        # AUTOMATIZACIÓN 1: ABRIR PÁGINA WEB
        print("\n[AUTOMATIZADO] Abriendo pagina web...")
        driver.get("https://www.wikipedia.org")
        time.sleep(3)
        print("[AUTOMATIZADO] Pagina cargada correctamente")
        
        # AUTOMATIZACIÓN 2: BUSCAR TEXTO ESPECÍFICO
        print("\n[AUTOMATIZADO] Buscando texto especifico...")
        search_text = "technology"
        
        # Encontrar campo automáticamente
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "searchInput"))
        )
        
        # Automatizar escritura
        search_box.clear()
        search_box.send_keys(search_text)
        print(f"[AUTOMATIZADO] Texto '{search_text}' ingresado")
        
        # Automatizar clic en buscar
        search_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        search_button.click()
        time.sleep(3)
        
        # Verificar resultado automáticamente
        page_title = driver.find_element(By.TAG_NAME, "h1").text
        print(f"[AUTOMATIZADO] Resultado encontrado: {page_title}")
        
        # AUTOMATIZACIÓN 3: CAPTURAR PANTALLA
        print("\n[AUTOMATIZADO] Capturando pantalla...")
        screenshot_path = "/app/screenshots/evidence.png"
        driver.save_screenshot(screenshot_path)
        print(f"[AUTOMATIZADO] Captura guardada: {screenshot_path}")
        
        # EVIDENCIA DE AUTOMATIZACIÓN
        current_url = driver.current_url
        print(f"\n[AUTOMATIZADO] URL final: {current_url}")
        print(f"[AUTOMATIZADO] Proceso completado automaticamente")
        
        return True
        
    except Exception as e:
        print(f"[AUTOMATIZADO] Error: {e}")
        driver.save_screenshot("/app/screenshots/error_evidence.png")
        return False
        
    finally:
        driver.quit()
        print("[AUTOMATIZADO] Navegador cerrado automaticamente")

if __name__ == "__main__":
    print("=" * 60)
    print("AUTOMATIZACION DE SELENIUM CON DOCKER")
    print("=" * 60)
    
    # EJECUTAR AUTOMATIZACIÓN COMPLETA
    success = automated_web_test()
    
    print("\n" + "=" * 60)
    if success:
        print("AUTOMATIZACION EXITOSA - Script ejecutado por Docker")
        print("Evidencia generada automaticamente")
        print("Proceso 100% automatizado")
    else:
        print("AUTOMATIZACION FALLO - Revisar logs")
    print("=" * 60)