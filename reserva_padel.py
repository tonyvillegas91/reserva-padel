from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time
import pyautogui  # Importamos PyAutoGUI
from datetime import datetime

# Verificar variables de entorno
print(f"DEBUG: PADDEL_USER={os.getenv('PADDEL_USER')}")
print(f"DEBUG: PADDEL_PASS={os.getenv('PADDEL_PASS')}")

# Cargar credenciales desde variables de entorno
usuario = os.getenv("PADDEL_USER")
contraseña = os.getenv("PADDEL_PASS")
if not usuario or not contraseña:
    raise ValueError("❌ ERROR: Las credenciales no están definidas. Usa 'export PADDEL_USER=usuario' y 'export PADDEL_PASS=contraseña' antes de ejecutar el script.")

# Configura la ubicación de ChromeDriver
chromedriver_path = "/usr/bin/chromedriver"
if not os.path.exists(chromedriver_path):
    raise FileNotFoundError(f"❌ ChromeDriver no encontrado en {chromedriver_path}.")

# Crear un objeto Service para ChromeDriver
service = Service(executable_path=chromedriver_path)

# Configura las opciones de Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")  # Maximizar la ventana para facilitar la detección de coordenadas
options.add_argument("--disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("--disable-gpu")

# Inicializa el WebDriver con el servicio y las opciones
driver = webdriver.Chrome(service=service, options=options)

# Abre la página de login
driver.get("https://private.tucomunidapp.com/login")
wait = WebDriverWait(driver, 20)  # Aumentamos el tiempo de espera a 20 segundos

try:
    # Inicio de sesión
    email_field = wait.until(EC.presence_of_element_located((By.NAME, "ion-input-0")))
    password_field = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='ion-input-1']")))
    email_field.send_keys(usuario)
    password_field.send_keys(contraseña)
    time.sleep(1)
    login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "ion-button.button")))
    login_button.click()
    print("✅ Inicio de sesión realizado con éxito.")
    time.sleep(5)

    # Botón Reservar
    reservar_button = wait.until(EC.presence_of_element_located((By.XPATH, "//ion-button[contains(., 'Reservar')]")))
    driver.execute_script("arguments[0].scrollIntoView();", reservar_button)
    reservar_button.click()
    print("✅ Botón de Reservar clicado con éxito.")
    time.sleep(5)

    # Selección del calendario
    calendario_icon = wait.until(EC.element_to_be_clickable((By.XPATH, "//ion-icon[@name='calendar-outline']")))
    driver.execute_script("arguments[0].click();", calendario_icon)
    print("✅ Icono del calendario clicado.")

    # Esperar a que el calendario esté completamente cargado
    wait.until(EC.visibility_of_element_located((By.XPATH, "//ion-datetime")))
    print("✅ Calendario cargado completamente.")

    # Obtener el host del Shadow DOM
    shadow_host = driver.find_element(By.XPATH, "//ion-datetime")

    # Seleccionar el día en el calendario usando JavaScript
    script = """
        const shadowHost = arguments[0];
        const shadowRoot = shadowHost.shadowRoot;
        const diaElemento = shadowRoot.querySelector('button[data-day="21"][data-month="2"][data-year="2025"]');
        if (diaElemento) {
            diaElemento.scrollIntoView({ block: 'center', inline: 'center' });
            diaElemento.click();
            return true;
        } else {
            return false;
        }
    """
    dia_seleccionado = driver.execute_script(script, shadow_host)
    if dia_seleccionado:
        print("✅ Día 21 de febrero de 2025 seleccionado correctamente.")
    else:
        raise Exception("❌ No se pudo encontrar el día 21 en el calendario.")

    # Hacer clic en el botón "Establecer"
    establecer_button = driver.find_element(By.XPATH, "//ion-button[contains(., 'Establecer')]")
    driver.execute_script("arguments[0].click();", establecer_button)
    print("✅ Botón 'Establecer' clicado.")

    # Esperar a que la pantalla original recargue antes de seleccionar la hora
    time.sleep(3)
    wait.until(EC.presence_of_element_located((By.XPATH, "//ion-label[contains(text(), '09:00 - 10:30')]")))

    # Selección de la hora
    hora_label = driver.find_element(By.XPATH, "//ion-label[contains(text(), '09:00 - 10:30')]")
    driver.execute_script("arguments[0].scrollIntoView();", hora_label)
    hora_label.click()
    print("✅ Hora 09:00 - 10:30 seleccionada.")

    # Función para esperar hasta una hora específica
    def esperar_hasta(hora_objetivo):
        while True:
            ahora = datetime.now().strftime("%H:%M:%S")
            if ahora >= hora_objetivo:
                print(f"✅ Hora alcanzada: {hora_objetivo}. Continuando...")
                break
            else:
                print(f"ℹ️ Esperando hasta {hora_objetivo}. Hora actual: {ahora}")
                time.sleep(0.7)  # Revisar cada 10 segundos

    # Programar el clic en el botón "Reservar" para las 17:20
    print("ℹ️ Programando clic en el botón 'Reservar' para las 10:30:00...")
    esperar_hasta("10:30:00")

    # Simular clic en el botón "Reservar" usando PyAutoGUI
    reservar_x, reservar_y = 985, 912  # Coordenadas reales del botón "Reservar"
    print("ℹ️ Haciendo clic en el botón 'Reservar' usando PyAutoGUI...")
    pyautogui.click(reservar_x, reservar_y)
    print("✅ Botón 'Reservar' clicado con éxito usando PyAutoGUI.")

    # Programar el clic en el botón "Aceptar" para justo después de hacer clic en "Reservar"
    print("ℹ️ Programando clic en el botón 'Aceptar'...")
    time.sleep(0.4)  # Pequeña pausa para asegurar que aparezca la ventana emergente

    # Simular clic en el botón "Aceptar" usando PyAutoGUI
    aceptar_x, aceptar_y = 993, 838  # Coordenadas reales del botón "Aceptar"
    print("ℹ️ Haciendo clic en el botón 'Aceptar' usando PyAutoGUI...")
    pyautogui.click(aceptar_x, aceptar_y)
    print("✅ Botón 'Aceptar' clicado con éxito usando PyAutoGUI.")

except Exception as e:
    print(f"❌ Error durante la ejecución: {e}")
finally:
    print("✅ Proceso completado.")
    # driver.quit()