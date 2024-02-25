# Hierarchy Ants Detector App

Este es un programa simple de inteligencia artificial que utiliza un modelo YOLOv8 entrenado con imágenes de hormigas de distintas jerarquías: obreras pequeñas (minor), obreras medianas (medior), obreras grandes o soldados (soldier), reinas (queen) y huevos (eggs). La aplicación permite cargar un archivo de video y realizar diferentes acciones de análisis sobre él utilizando el modelo de detección de hormigas.

## Requisitos

Asegúrate de tener instaladas todas las dependencias necesarias para ejecutar la aplicación. Puedes instalarlas ejecutando:

```bash
pip install -r requirements.txt
```

## Uso

Para ejecutar la aplicación, simplemente ejecuta el script `main.py`:

```bash
python main.py
```

Una vez ejecutado, se te pedirá que selecciones un archivo de video. Después, se abrirá una ventana con un botón para realizar la siguiente acción:

- **Detectar:** Realiza la detección de hormigas en el video cargado.

## Créditos

Este proyecto utiliza un modelo YOLOv8 entrenado con imágenes de hormigas proporcionadas por Roboflow.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar esta aplicación, por favor envía un pull request.