# Proyecto de Simulación de Zombies en un Edificio

## Instalación y Ejecución

1. **Instalación de Python:**

   Si no tienes Python instalado, puedes seguir estos pasos:

   - **Para Windows:**
     1. Visita la página oficial de [Python](https://www.python.org/downloads/).
     2. Haz clic en "Download Python" para obtener la última versión estable.
     3. Durante la instalación, **asegúrate de marcar la opción "Add Python to PATH"**.
     4. Una vez instalado, abre la terminal (CMD o PowerShell) y ejecuta:
        ```bash
        python --version
        ```
        Esto debería mostrar la versión de Python instalada.

   - **Para macOS:**
     1. Abre la terminal.
     2. Puedes instalar Python utilizando [Homebrew](https://brew.sh/). Si no tienes Homebrew instalado, primero instala Homebrew con el siguiente comando:
        ```bash
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        ```
     3. Luego, instala Python con el comando:
        ```bash
        brew install python
        ```
     4. Verifica la instalación con:
        ```bash
        python3 --version
        ```

   - **Para Linux:**
     1. Abre la terminal.
     2. En distribuciones basadas en Debian (como Ubuntu), puedes instalar Python con el siguiente comando:
        ```bash
        sudo apt update
        sudo apt install python3
        ```
     3. Verifica la instalación con:
        ```bash
        python3 --version
        ```

2. **Cómo ejecutar la aplicación:**
   - Descarga o clona este repositorio.
   - En la terminal, navega hasta el directorio del proyecto.
   - Ejecuta el siguiente comando:
     ```bash
     python main.py
     ```

3. **Instrucciones de uso:**
   - Al ejecutar el archivo, se abrirá un menú interactivo en la terminal.
   - El usuario podrá elegir entre varias opciones para simular el movimiento de zombies en un edificio, como configurar el edificio, mover zombies, bloquear habitaciones, entre otros.

---

## Arquitectura y Clases

La aplicación simula el movimiento de zombies en un edificio con múltiples pisos y habitaciones. El edificio está compuesto por pisos, y cada piso tiene varias habitaciones, cada una con un sensor que puede ser activado, bloqueado o reseteado. 

1. **Clases principales:**
   - **Sensor:** Representa el sensor de una habitación. Puede estar en estado "normal", "alerta" o "bloqueado". 
   - **Room:** Representa una habitación en un piso. Controla el número de zombies presentes y el estado del sensor de la habitación.
   - **Floor:** Representa un piso del edificio, que contiene varias habitaciones. También tiene un contador de zombies en total.
   - **Building:** Representa el edificio, compuesto por varios pisos. Permite añadir zombies manualmente o aleatoriamente, y moverlos entre habitaciones.
   - **Simulation:** Controla la simulación. Permite configurar el edificio, mostrar su estado, mover zombies, y realizar acciones sobre las habitaciones (limpiar, bloquear, desbloquear, resetear sensores, etc.).

2. **Comportamiento:**
   - El simulador permite interactuar con el edificio, mover zombies de una habitación a otra aleatoriamente y realizar varias acciones sobre las habitaciones, como bloquearlas, limpiarlas o resetear el sensor.
   - También es posible agregar zombies de manera manual o aleatoria, y visualizar el estado actual del edificio en cualquier momento.

---

## Comandos de Uso

**Menú Principal:**
- **1. Configurar edificio:** Establece el número de pisos y habitaciones por piso.
- **2. Mostrar estado del edificio:** Muestra el estado actual de todas las habitaciones del edificio.
- **3. Mover zombies:** Mueve los zombies de una habitación a otra aleatoriamente dentro del mismo piso.
- **4. Limpiar habitación:** Elimina los zombies de una habitación seleccionada.
- **5. Bloquear habitación:** Bloquea el sensor de una habitación para que no pueda activarse.
- **6. Resetear sensor:** Resetea el sensor de una habitación, poniéndolo en su estado original.
- **7. Agregar zombies:** Permite agregar zombies aleatoriamente a las habitaciones del edificio.
- **8. Desbloquear habitación:** Desbloquea el sensor de una habitación.
- **9. Salir:** Finaliza la simulación.

---
