# Cómo crear un entorno virtual de Python en Visual Studio Code (Windows)

Este documento explica cómo crear y activar un entorno virtual de Python para tu proyecto en Windows usando Visual Studio Code.

## Pasos

### 1. Abre tu proyecto en Visual Studio Code

- Abre la carpeta de tu proyecto existente o crea una nueva desde Visual Studio Code.

### 2. Abre la terminal integrada

- Ve a `Ver > Terminal` en la barra de menú superior,  
  o presiona `` Ctrl + ` `` (la tecla de tilde invertida).

### 3. Crea el entorno virtual

En la terminal, ejecuta el siguiente comando:

`python -m venv venv`

### 4. Activa el entorno virtual

`.\venv\Scripts\activate`

### 5. Selecciona el intérprete de Python en Visual Studio Code

Haz clic en la parte inferior derecha (o izquierda) donde aparece la versión de Python,
o presiona Ctrl+Shift+P y busca "Python: Seleccionar intérprete".

Selecciona el intérprete de Python que está dentro de la carpeta venv
(debería verse algo como .\venv\Scripts\python.exe)

### NOTAS

deactivate

pip install nombre_del_paquete