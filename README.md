# MOVIE API

## Configuración

Se debe generar un entorno virtual con el siguiente comando:
```bash
python3 -m venv venv
```
Donde el segundo `venv` es el nombre del entorno. Luego, activarlo (en entorno Linux) con este comando:

```bash
source venv/bin/activate
```
Se puede desactivar el entorno virtual, con:

```bash
deactivate
```
Instalar las dependencias de la aplicación con pip:

```bash
python3 -m pip install -r requirements.txt
```
Acá el archivo `requirements.txt` puede ser agregado al controlador de versiones y distribuido como parte de la aplicación para saber qué se debe de instalar.

Si  dicho archivo no existe, se crea con:

```bash
python3 -m pip freeze > requirements.txt
```
También se pueden ver los paquetes o dependencias instaladas en el entorno virtual con el comando:

```bash
python3 -m pip list
```

## Ejecución del Proyecto

Ahora para iniciar el proyecto se deben ejecutar los siguientes comandos en la terminal:

```bash
uvicorn main:app --reload
```
Donde `main` es el nombre del módulo principal y `app` es el nombre de la función que contiene la app FastAPI. Opcionalmente si queremos correrlo y que por cada cambio detectado en el código se recargue en tiempo real se agrega el parámetro `--reload`.

Para detener el servidor basta con presionar `Ctrl + C`.
