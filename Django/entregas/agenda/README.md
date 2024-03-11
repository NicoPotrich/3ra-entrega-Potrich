# Agenda de Django

Este es un proyecto de agenda desarrollado en Django que permite gestionar contactos, tareas y reuniones.

## Características

- **Gestión de Contactos**: Permite crear, ver, editar y eliminar contactos. Cada contacto puede tener un nombre, apellido, dirección, número de teléfono y correo electrónico.

- **Gestión de Tareas**: Permite crear, ver, editar y eliminar tareas pendientes. Cada tarea puede tener un título, descripción, fecha estimada de finalizacion y nivel de prioridad

- **Gestión de Reuniones**: Permite crear, ver, editar y eliminar reuniones. Cada reunión puede tener un título, descripción, fecha y hora de inicio y finalización y lista de participantes.

## Organización del Proyecto

El proyecto está organizado en tres aplicaciones principales:

1. **Contactos**: Gestiona la información de contactos.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/contact`.py

2. **Tareas**: Gestiona las tareas pendientes.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/todo`.

3. **Reuniones**: Gestiona las reuniones programadas.
   - Archivos relevantes: `models.py`, `views.py`, `forms.py`, `urls.py`, `templates/meetings`.

Otros archivos importantes incluyen:

- `settings.py`: Configuración del proyecto Django.
- `urls.py`: Definición de las URL del proyecto.
- `templates/`: Plantillas HTML para las vistas.

## Backend vs. Frontend

Este proyecto se enfoca principalmente en el backend, con una mínima parte del frontend. La mayoría de las funcionalidades y lógica están implementadas en el backend utilizando Django y Python, mientras que el frontend consiste principalmente en plantillas HTML simples para representar los datos.

## Instalación y Uso

1. Clona este repositorio: `git clone https://ruta/a/tu/repositorio.git`
2. Instala las dependencias: `pip install -r requirements.txt`
3. Realiza las migraciones de la base de datos: `python manage.py migrate`
4. Inicia el servidor de desarrollo: `python manage.py runserver`

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes sugerencias o mejoras para este proyecto, no dudes en abrir un issue o enviar un pull request.