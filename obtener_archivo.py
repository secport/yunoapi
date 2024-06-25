import requests
import sys
from datetime import datetime

#Función que recibe el archivo CSV cuando hace la consulta al endpoint de la API, en caso de que no exista el archivo correspondiente a la IP se recibe un mensaje de error
def obtener_csv(ip, api_server_ip):
    url = f"http://{api_server_ip}:5000/api/data/{ip}"
    response = requests.get(url)
    
    if response.status_code == 200:
        nombre_archivo = f"{ip}_{datetime.now().strftime('%Y-%m-%d')}.csv"
        with open(nombre_archivo, 'wb') as archivo:
            archivo.write(response.content)
        print(f"Archivo CSV guardado como {nombre_archivo}")
    else:
        print(f"Error: {response.status_code}, {response.text}")

#Función main para ejecución de la APP y recibir el archivo CSV o la respuesta de error
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python obtener_archivo.py <DIRECCION_IP_MAQUINA> <DIRECCION_IP_API>")
        sys.exit(1)
    
    ip = sys.argv[1]
    ip_api = sys.argv[2]
    obtener_csv(ip, ip_api)
