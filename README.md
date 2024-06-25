El sistema construido está compuesto por lo siguiente:

1.	Aplicación agente (**agente.py**, **agente_windows.py**), la cual se ejecuta en el servidor del cual se requiere recolectar la información para que sea enviada a la API donde se centraliza la información.
2.	Aplicación API (**api.py**) construida con Flask, la cual se ejecuta en un servidor desplegado en instancia EC2 de AWS donde se centraliza la información de los distintos agentes.
3.	Aplicación para obtener el archivo CSV correspondiente a una dirección IP de la cual se haya recogido información en el servidor donde se encuentra la API (**obtener_archivo.py**). Esta aplicación se puede ejecutar desde cualquier sistema siempre y cuando se pase como parámetro la dirección IP de la máquina de la cual se quiere obtener el archivo CSV y la dirección IP del servidor donde corre la API.


*********************************************************************
**Requisitos para ejecutar aplicaciones que se comunican con la API**
*********************************************************************

**LINUX**

Actualizar repositorios sistema operativo e instalación de Python 3

>sudo apt-get update

>sudo apt-get install python3


**WINDOWS**

Descargar e instalar Python3 desde sitio oficial https://www.python.org/downloads/


******************************************************************
**Sintáxis ejecución de aplicaciones que se comunican con la API**
******************************************************************

**Agente Linux**

>python3 agente.py <API_IP>

**Agente Windows**

>python3 agente_windows.py <API_IP>

**Obtener Archivo**

>python3 obtener_archivo.py <DIRECCION_IP_MAQUINA> <API_IP>

<API_IP> corresponde a la dirección IP del servidor donde está corriendo la API.

<DIRECCION_IP_MAQUINA> corresponde a la dirección IP de la máquina de la cual se quiere obtener el archivo CSV.

**NOTA IMPORTANTE:** Para equipos **Linux**, la dirección IP local se obtiene con la ejecución del comando **hostname -I** desde una terminal Bash. 
Para equipos **Windows**, la dirección IP local se obtiene con la ejecución del comando **socket.gethostbyname(socket.gethostname())** desde una consola de Python3 (se debe importar la librería **socket**).

*******************************************
**Implementación de API en servidor Linux**
*******************************************

**NOTA**: La aplicación API está desarrollada y probada su implementación en un servidor Linux Debian, para otras plataformas y sistemas operativos no ha sido probada la implementación.

Para la aplicación API se despliega un servdor Linux Debian en AWS EC2 con las características correspondientes a la capa gratuita.

Se debe habilitar como regla de entrada el puerto 5000 para que se tenga comunicación con la API.

**A continuación el paso a paso para implementar la API:**

Actualizar repositorios sistema operativo
>sudo apt-get update

Instalar Python3
>sudo apt-get install python3

Instalar VENV para montar la API en un entorno virtual
>sudo apt install python3-venv

Crear el entorno virtual
>mkdir myproject

>cd myproject

>python3 -m venv env

Activar el entorno virtual (estando en la carpeta del proyecto)

>. env/bin/activate

Instalar Flask (validar que la terminal ahora aparezca que inicia con la palabra **(env)**)

>pip install flask

Ejecutar API

>python3 api.py
