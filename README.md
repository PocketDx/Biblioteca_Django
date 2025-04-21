# 📚 Biblioteca_Django
 Introducción a Django: modelos y el administrador

## 🛠 Requisitos

* Entorno Virtual (Recomendado)
* Python 3.13
* Django 5.2

### ✨ Funcionalidad

Este proyecto es una aplicación web usando Django que permite:
    
* Registrar autores y libros
* Registrar reseñas para cada libro
    * Visualizar libros y reseñas

## 🕹 Instalación

1. Clonar el repositorio:
    ```bash
    git clone https://github.com/PocketDx/Biblioteca_Django.git

    cd biblioteca_project
    ```
2. Crea un entorno virtual y activalo (Windows)
    ```
    python -m venv venv
    .venv\Scripts\activate
    ```

3. Instalar las dependencias:
    ```
    pip install -r requirements.txt
    ```
4. Prepara la ejecución
    ```
    python manage.py migrate  #Aplica las migraciones
    python manage.py createsuperuser  # Crear un super usuario (Opcional)
    python manage.py runserver  # Corre el servidor

    ```

## 🎮 Ejecutar El Proyecto

1. Abrir el navegador 
    
* Accede a la app desde http://127.0.0.1:8000/

* Usa el panel de administración en http://127.0.0.1:8000/admin/ para gestionar los modelos
    
    ```
    usuario: admin
    clave: 1234COCO
    ```

# Capturas de Pantalla (Script y Panel Admin)

[![Script.jpg](https://i.postimg.cc/fLzDrp0D/Script.jpg)](https://postimg.cc/DWM9WCgM)
---
[![Panel-Admin.jpg](https://i.postimg.cc/G2wq3njn/Panel-Admin.jpg)](https://postimg.cc/sBmpK88T)

> Este proyecto se desarrolla desde una practica academica, siguiendo algunas instrucciones del docente, complementado por videos de Youtube y usando ChatGPT como apoyo en consultas sobre conceptos desconocidos. Por lo cual este podría contener errores.