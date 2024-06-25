import os
import platform
import requests
import json
import sys

#A continuación las funciones para la obtención de la información del Sistema Operativo
def obtener_info_procesador():
    return platform.machine()

def obtener_procesos_corriendo():
    return os.popen('ps aux').read()

def obtener_usuarios_logueados():
    return os.popen('who').read()

def obtener_nombre_so():
    return platform.system()

def obtener_version_so():
    return platform.version()

def obtener_ip_servidor():
    return os.popen('hostname -I | tr -d "[[:space:]]"').read()

#Función donde se recolecta la información utilizando las funciones anteriores y se almacena en un objeto DICT de Python
def recolectar_info():
    info = {
        'procesador': obtener_info_procesador(),
        'procesos': obtener_procesos_corriendo(),
        'usuarios': obtener_usuarios_logueados(),
        'nombre_so': obtener_nombre_so(),
        'version_so': obtener_version_so(),
        'ip': obtener_ip_servidor()
    }
    return info

#Función para envío de la información parseada a formato JSON a la API ubicada en instancia EC2 de AWS
def envio_info_api(info, api_ip):
    url = f"http://{api_ip}:5000/api/data"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, data=json.dumps(info), headers=headers)
    return response

#Función main para ejecución de la APP agente y recibir respuestas de la API
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python agente_windows.py <DIRECCION_IP_API>")
        sys.exit(1)
    
    ip_api = sys.argv[1]
    info = recolectar_info()
    response = envio_info_api(info, ip_api)
    print(response.json())
    print(f"Código de estado HTTP: {response.status_code}")