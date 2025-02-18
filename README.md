# Automatización de Reserva de Pistas de Pádel

Este programa automatiza el proceso de reserva de pistas de pádel en la plataforma [TuComunidadApp](https://private.tucomunidapp.com/login). Utiliza Selenium para interactuar con elementos web y PyAutoGUI para simular clics en botones específicos que Selenium no puede manejar directamente.

---

## Contenido del Repositorio

- `reserva_padel.py`: Script principal que realiza la reserva.
- `Makefile`: Archivo para automatizar la configuración y ejecución del script.
- `.gitignore`: Lista de archivos ignorados por Git (por ejemplo, `.env` y entornos virtuales).
- `README.md`: Documentación del proyecto.

> **Nota**: El archivo `.env` no está incluido en este repositorio por razones de seguridad. Debes crearlo manualmente con tus propias credenciales.

---

## Requisitos

- Python 3.10 o superior.
- ChromeDriver instalado y compatible con tu versión de Google Chrome.
- Dependencias: `selenium`, `pyautogui`.
- Sistema operativo: Linux o macOS (debido al uso de PyAutoGUI y X11).

---

## Instalación

### **En Linux**

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tonyvillegas91/reserva-padel.git
   cd reserva-padel
   ```

2. **Instalar ChromeDriver:**  
   - Descarga la versión correcta de ChromeDriver desde el sitio oficial.
   - Coloca el archivo `chromedriver` en `/usr/bin/` o en otra ruta accesible.
   ```bash
   sudo mv chromedriver /usr/bin/
   ```

3. **Crear un Entorno Virtual:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. **Instalar Dependencias:**
   ```bash
   pip install selenium pyautogui
   ```

5. **Configurar Variables de Entorno:**  
   Crea un archivo `.env` con tus credenciales:
   ```ini
   PADDEL_USER1=usuario1@example.com
   PADDEL_PASS1=contraseña1
   PADDEL_USER2=usuario2@example.com
   PADDEL_PASS2=contraseña2
   ```
   Asegúrate de que el archivo `.env` tenga permisos adecuados:
   ```bash
   chmod 644 .env
   ```

6. **Configurar Permisos X11 (solo para Linux):**
   ```bash
   xhost +
   xhost +si:localuser:$USER
   ```

7. **Ejecutar el Script:**
   Usa el `Makefile` para ejecutar el programa:
   ```bash
   make run USER_INDEX=1
   ```
   Cambia `USER_INDEX` según el usuario que quieras utilizar (por ejemplo, `USER_INDEX=2`).

---

### **En macOS**

1. **Clonar el Repositorio:**
   ```bash
   git clone https://github.com/tonyvillegas91/reserva-padel.git
   cd reserva-padel
   ```

2. **Instalar ChromeDriver:**  
   - Descarga la versión correcta de ChromeDriver desde el sitio oficial.
   - Coloca el archivo `chromedriver` en una carpeta accesible, como `/usr/local/bin/`.
   ```bash
   sudo mv chromedriver /usr/local/bin/
   ```

3. **Crear un Entorno Virtual:**
   ```bash
   python3 -m venv myenv
   source myenv/bin/activate
   ```

4. **Instalar Dependencias:**
   ```bash
   pip install selenium pyautogui
   ```

5. **Configurar Variables de Entorno:**  
   Crea un archivo `.env` con tus credenciales:
   ```ini
   PADDEL_USER1=usuario1@example.com
   PADDEL_PASS1=contraseña1
   PADDEL_USER2=usuario2@example.com
   PADDEL_PASS2=contraseña2
   ```
   Asegúrate de que el archivo `.env` tenga permisos adecuados:
   ```bash
   chmod 644 .env
   ```

6. **Ejecutar el Script:**
   Usa el `Makefile` para ejecutar el programa:
   ```bash
   make run USER_INDEX=1
   ```
   Cambia `USER_INDEX` según el usuario que quieras utilizar (por ejemplo, `USER_INDEX=2`).

---

## Uso

1. **Seleccionar Usuario:**  
   Usa el parámetro `USER_INDEX` para seleccionar el usuario deseado.
   ```bash
   make run USER_INDEX=1
   ```
   Para el usuario 2:
   ```bash
   make run USER_INDEX=2
   ```

2. **Programar la Ejecución:**  
   - El script espera hasta una hora específica (configurable en el código) antes de hacer clic en el botón "Reservar".
   - Después de presionar "Reservar", el script hace clic automáticamente en "Aceptar".
   
3. **Dependencias de PyAutoGUI:**  
   - **En Linux**, instala las siguientes dependencias:
     ```bash
     sudo apt update
     sudo apt install -y python3-tk scrot
     ```
   - **En macOS**, podría ser necesario instalar `pyobjc`:
     ```bash
     pip install pyobjc
     ```

---

## Personalización del Script

Puedes modificar el código para ajustar las siguientes configuraciones según tus necesidades:

1. **Fecha de la Reserva**  
   - En el script, encontrarás una sección donde puedes especificar la fecha exacta para la reserva.
   
2. **Horario de la Reserva**  
   - Puedes definir el horario en el que deseas reservar la pista.

3. **Hora del Último Clic**  
   - Para asegurarte de que la reserva se haga en el momento exacto, puedes establecer la hora en la que el script ejecutará el último clic en el botón de reserva.

Busca los comentarios en el código donde se indica cada uno de estos ajustes y personalízalos según tus preferencias.

---

## Licencia

Este proyecto está licenciado bajo la Licencia MIT. Consulta el archivo `LICENSE` para más detalles.
