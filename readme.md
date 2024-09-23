# Sistema de Gestión de Tareas

Este proyecto es un sistema simple de gestión de tareas en Python que permite a los usuarios agregar, actualizar, eliminar, ver y marcar tareas como completadas. Cada tarea contiene un título, una descripción y un estado (pendiente o completada).

## Índice

- [Instalación](#instalación)
  - [Instalar Python](#instalar-python)
  - [Instalar pip](#instalar-pip)
  - [Instalar dependencias](#instalar-dependencias)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Descripción de Archivos](#descripción-de-archivos)
- [Cómo ejecutar el proyecto](#cómo-ejecutar-el-proyecto)
- [Cómo ejecutar los tests](#cómo-ejecutar-los-tests)
- [Explicación del código](#explicación-del-código)
- [Ver el video del proyecto](#ver-el-video-del-proyecto)
- [Integrantes](#integrantes)

## Instalación

### Instalar Python

Para ejecutar este proyecto, necesitas tener Python instalado en tu máquina. Puedes descargar la última versión de Python desde el sitio oficial:

[Descargar Python](https://www.python.org/downloads/)

Asegúrate de que la opción `Add Python to PATH` esté seleccionada durante la instalación.

### Instalar pip

Si no tienes `pip` (el gestor de paquetes de Python) instalado, sigue estos pasos para instalarlo:

1. Descarga el script `get-pip.py` desde [este enlace](https://bootstrap.pypa.io/get-pip.py).
2. En la terminal, navega al directorio donde descargaste el archivo y ejecuta:

   ```bash
   py get-pip.py
   ```

3. Verifica que `pip` se instaló correctamente ejecutando:

   ```bash
   pip --version
   ```

### Instalar dependencias

Una vez que tengas `pip` instalado, instala las dependencias del proyecto. Estas se especifican en el archivo `requirements.txt`:

```text
unittest
pytest
```

Para instalar las dependencias, ejecuta:

```bash
pip install -r requirements.txt
```

## Estructura del Proyecto

```plaintext
Sistema_gestion/
│
├── src/
│   ├── __init__.py          # Inicialización del paquete
│   ├── main.py              # Punto de entrada principal del sistema
│   ├── task.py              # Funciones para la gestión de tareas
│
├── test/
│   ├── __init__.py          # Inicialización del paquete de pruebas
│   └── test_task.py         # Archivo de pruebas para las funcionalidades
│
├── video/                   # Carpeta que contiene la explicación en video
│   └── explicacion_proyecto.mp4  # Video explicativo del proyecto
│
├── .gitignore               # Archivos que serán ignorados por Git
├── readme.md                # Este archivo de documentación
└── requirements.txt         # Archivo con las dependencias del proyecto
```

## Descripción de Archivos

### `/src/`
- **`__init__.py`**: Archivo de inicialización del paquete `src`.
- **`main.py`**: Contiene el menú principal del sistema, que permite a los usuarios interactuar con el sistema de gestión de tareas.
- **`task.py`**: Contiene las funciones para agregar, actualizar, eliminar, ver y marcar tareas como completadas.

### `/test/`
- **`__init__.py`**: Archivo de inicialización del paquete `test`.
- **`test_task.py`**: Contiene los tests para simular la interacción de un usuario con el sistema, como agregar tareas, actualizarlas, eliminarlas, verlas y marcarlas como completadas.

### `/video/`
- **`explicacion_proyecto.mp4`**: Este es un video explicativo del proyecto, que detalla su funcionamiento y los principales aspectos del código. El video está almacenado en esta carpeta y se puede visualizar directamente en este README.

### Otros Archivos
- **`.gitignore`**: Este archivo contiene las reglas para evitar que ciertos archivos y directorios sean rastreados por Git.
- **`readme.md`**: Este archivo de documentación que explica cómo funciona el proyecto y cómo instalarlo.
- **`requirements.txt`**: Lista las dependencias necesarias para ejecutar el proyecto. Aquí se incluyen las herramientas de pruebas como `unittest` y `pytest`.

## Cómo ejecutar el proyecto

Para ejecutar el sistema de gestión de tareas, sigue estos pasos:

1. Abre una terminal o consola.
2. Navega al directorio donde se encuentra el archivo `main.py` del proyecto.
3. Ejecuta el siguiente comando:

   ```bash
   py -m src.main
   ```

Esto iniciará el sistema, donde podrás interactuar con el menú para agregar, actualizar, eliminar, ver y marcar tareas como completadas.

## Cómo ejecutar los tests

Para ejecutar los tests, sigue estos pasos:

1. Navega al directorio raíz del proyecto (donde se encuentra la carpeta `test`).
2. Ejecuta el siguiente comando:

   ```bash
   py -m unittest discover -s test
   ```

Esto ejecutará todos los tests y te permitirá verificar que las funcionalidades del sistema funcionan correctamente.

### Descripción de los tests

El archivo `test_task.py` contiene tests que simulan la interacción de un usuario con el sistema de gestión de tareas. El flujo del test incluye los siguientes pasos:

1. **Agregar dos tareas**:
   - Tarea 1: "Comprar víveres".
   - Tarea 2: "Terminar proyecto".
2. **Ver todas las tareas**: El sistema lista las dos tareas agregadas.
3. **Actualizar la segunda tarea**:
   - El título de la segunda tarea cambia a "Actualizar proyecto".
   - La descripción de la segunda tarea cambia a "Añadir documentación al proyecto".
4. **Verificar la actualización**: El sistema muestra las dos tareas, incluida la tarea actualizada.
5. **Eliminar la primera tarea**: El sistema elimina la tarea "Comprar víveres".
6. **Verificar la lista de tareas**: El sistema muestra solo la tarea actualizada.
7. **Salir del programa**: El test finaliza cerrando el programa.

## Ver el video del proyecto

Puedes ver el video explicativo del proyecto en el siguiente enlace. Este video detalla el funcionamiento del sistema de gestión de tareas, su estructura y los aspectos clave del código.

[Ver el video explicativo del proyecto](https://unisalleedu-my.sharepoint.com/:v:/g/personal/juperez49_unisalle_edu_co/ES6TcUslu2RGobRBWNWp38oB00aJaq6JBFd43-K5u4A5dA)


## Integrantes

- **Anner Alexis Carabali Banguera** - acarabali68@unisalle.edu.co
- **Andres Felipe Rodriguez Martinez** - androdriguez48@unisalle.edu.co
- **Juan David Pérez Numa** - juperez49@unisalle.edu.co
