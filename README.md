# Projecto Ventas fundacion Corazones Peludos.


## Requisitos previos

Enumera aquí los requisitos previos o dependencias necesarios para el proyecto.

- Instalación de Python:

	Visita el sitio web oficial de Python en https://www.python.org/downloads/ 
	y descarga el instalador correspondiente a tu sistema operativo.
	Ejecuta el archivo de instalación descargado y sigue las instrucciones del instalador. 
	Asegúrate de marcar la casilla "Add Python to PATH" (Agregar Python al PATH) durante la instalación.
	Después de la instalación, abre una nueva ventana del CMD y 
	verifica que Python se haya instalado correctamente ejecutando el siguiente comando: python--version 

- Instalación de Django:

	Abre una nueva ventana del CMD.
	Ejecuta el siguiente comando para instalar Django utilizando el administrador de paquetes de Python, pip:
	codigo:
		--pip install django 
	Espera a que la instalación se complete. 
	Pip descargará e instalará la última versión estable de Django y sus dependencias.
	Para verificar que Django se haya instalado correctamente, ejecuta el siguiente comando:
		django-admin --version
	Esto mostrará la versión de Django instalada.

- Instalación de bootstrap4.
	Abre una ventana de comandos(CMD)y ejecuta el siguente comando : pip install django-bootstrap4
	Este comando instalará la biblioteca  Django-Bootstrap4 lo que permite la integración de bootstrap4 en Django
	
	Una vez completada la instalación, 
	abre el archivo settings.py en tu proyecto Django y agrega 'bootstrap4' a la lista de INSTALLED_APPS:
	Ejemplo:
	
		INSTALLED_APPS = [
    				...
    				'bootstrap4',
    				...
				]
	Para utilizar Bootstrap 4 en tus plantillas de Django, agrega la siguiente etiqueta de carga en la parte superior de tus archivos HTML:

		{% load bootstrap4 %}


- instalación de django-crispy-forms
	Abre una ventana de comandos (CMD) y navega hasta el directorio raíz de tu proyecto Django.
	Ejecuta el siguiente comando para instalar django-crispy-forms utilizando el administrador de paquetes de Python, pip:
		pip install django-crispy-forms
	Una vez completada la instalación, abre el archivo settings.py en tu proyecto Django y agrega 'crispy_forms' a la lista de INSTALLED_APPS:
		INSTALLED_APPS = [
    			...
    			'crispy_forms',
   			 ...
			]
	Para utilizar django-crispy-forms en tus formularios de Django, agrega la siguiente etiqueta de carga en la parte superior de tus archivos HTML:
		{% load crispy_forms_tags %}

	



## Créditos

	Luis Laborie.
	Paul Arellano

