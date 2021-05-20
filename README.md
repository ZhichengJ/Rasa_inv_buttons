# Chatbot Chatbot para Público Infantil para Clasificar Sonidos del Cielo

![ScreenShot](Chatbot-Widget/static/img/principal.png)

---

## Introducción

- El proyecto tiene como finalidad la implementación para ayudar a usuarios a clasificar sonidos de ecos captados mediante radiodetección.

---

## About

- Este proyecto ha sido desarrollado por [Marcos Pino](https://www.linkedin.com/in/marcos-pino-gamazo-800b4261/) como Trabajo de Fin de Grado en la [Universidad Politécnica de Madrid](https://www.upm.es/) para el grado de ingeniería informática de la [Escuela Técnica Superior de Ingenieros Informáticos](https://www.fi.upm.es) para el proyecto [Sonidos del Cielo](http://sonidosdelcielo.org/) del [Laboratorio de Ciencia Ciudadana](https://cslab-upm.github.io/index.html). La aplicación ***Chatbot Chatbot para Público Infantil para Clasificar Sonidos del Cielo*** tiene como finalidad la de ayudar a personas con poco contacto con la ciencia a participar en la clasificación de sonidos de ecos generados a partir de radiodetecciones. 

---

## Despliegue

- Antes que nada, tenemos que instalar [Docker](https://www.docker.com)

> Instalación en Windows

- Para instalar docker en windows, lo descargamos del siguiente [link](https://hub.docker.com/editions/community/docker-ce-desktop-windows/). 
- Cuando esté descargado, hacer doble-click en ``Docker for Windows Installer``para correr el instalador. 
- Al finalizar la instalación, se mostrará una indicación con un icono de ballena que señaliza que Docker está funcionando.

> Instalación en Linux

- Primero, actualizamos la lista de paquetes existente con el comando ``sudo apt update``
- A continuación, instalamos paquetes de requisitos previos para permitir a apt utilizar paquetes a través de HTTPS ``sudo apt install apt-transport-https ca-certificates curl software-properties-common``

- Después, añadir la clave GPG para el repositorio oficial de Docker ``curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -``
- Agregar el repositorio de Docker a las fuentes de APT ``sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
``
- A continuación, actualizar el paquete de base de datos con los paquetes de Docker del repositorio agregado ``sudo apt update``
- Por último, instalar Docker: ``sudo apt install docker-ce``

>Instalación en Mac

- Para instalar docker en macOS, lo descargamos del siguiente [link](https://hub.docker.com/editions/community/docker-ce-desktop-mac/). 
- Cuando esté descargado, hacer doble-click en ``Docker.img``para correr el instalador. 
- Al finalizar la instalación, se mostrará una indicación con un icono de ballena que señaliza que Docker está funcionando.

> Despliegue de los contenedores

- Una vez tengamos Docker instalado y hayamos clonado el proyecto, ejecutamos el siguiente comando:
```$ docker-compose up -d``` 

- De esta forma tendremos corriendo dos contenedores: uno para el Rasa Core y el otro con el servidor de acciones.

---

## Funcionamiento

- Cuando tengamos los dos contenedores corriendo, podremos consumir los servicios del asistente virtual a través de la siguiente URI(`POST`):  
```http://localhost:5005/webhooks/rest/webhook```

Para utilizar el chatbot, se recomienda el uso del frontal disponible en este [repositorio](https://github.com/cslab-upm/Chatbot-Widget)
