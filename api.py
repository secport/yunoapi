from flask import Flask, request, jsonify, send_file, abort
import csv
from datetime import datetime
import os

app = Flask(__name__)

#Establecimiento de ruta de la API y método HTTP utilizado para interactuar con la API para envío de información
@app.route('/api/data', methods=['POST'])
#Función que recibe la información en formato JSON y la almacena en un archivo CSV que en su nombre tiene la info de la IP donde se ejecutó el agente y la fecha actual en formato AAAA-MM-DD
def recibir_info():
    info= request.json
    ip = info.get('ip')
    fecha_str = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"{ip}_{fecha_str}.csv"
    
    #Se crea el archivo CSV con el nombre establecido, delimitador ; y se configura en modo escritura para incluir la información recibida
    with open(nombre_archivo, mode='w') as archivo:
        writer = csv.writer(archivo, delimiter=';')
        writer.writerow(['Procesador', 'Procesos', 'Usuarios', 'Nombre SO', 'Versión SO'])
        writer.writerow([info['procesador'], info['procesos'], info['usuarios'], info['nombre_so'], info['version_so']])
    
    #Respuesta para el cliente con mensaje en formato JSON y código de estado HTTP 200
    return jsonify({"Mensaje": "Datos recibidos"}), 200


#Establecimiento de ruta de la API y método HTTP utilizado para interactuar con la API para recibo de información
@app.route('/api/data/<ip>', methods=['GET'])
#Función que envía la información del archivo CSV correspondiente a la dirección IP que se recibe como parámetro
def envio_info(ip):
    fecha_str = datetime.now().strftime("%Y-%m-%d")
    nombre_archivo = f"{ip}_{fecha_str}.csv"
    
    #Se valida si el archivo existe y se envía, si no existe se envía un mensaje de error indicando que el Archivo no fue encontrado
    if os.path.exists(nombre_archivo):
        return send_file(nombre_archivo, as_attachment=True)
    else:
        abort(404, description="Archivo no encontrado")

if __name__ == "__main__":
    app.run(host='0.0.0.0')
