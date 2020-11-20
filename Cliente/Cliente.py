# importamos json
import json
# importamos request para el http
import requests
#importamos datetime
from datetime import datetime

# Archivo de Logs
Log=open("C:\\Users\\Moino\\Documents\\2do2020\\Sa\\lab\\practica3\\Cliente\\log.txt","w") 
# solicitamos el pedido a la url del pedido
url= "http://localhost:62499/api/pedido/3"
response = requests.get(url)
print(response)
#escribimos en el log
Log.write("fecha y hora: "+str(datetime.now())+" "+"\nPedido \n"+str(response.json())+" "+"\n") 

# pedido
pedido = response.json().get("id")
# cliente
cliente = response.json().get("idCliente")
# estado
estado = response.json().get("estado")
# escribimos en el log el pedido
Log.write("Revisar estado del Pedido \nfecha y hora: "+str(datetime.now())+"\n pedido: "+str(pedido)+"\n cliente: "+str(cliente)+" \n estado: "+str(estado)+" "+"\n")


urlagregar = "http://localhost:62499/api/pedido/agregar"
# variable headers que inidican en que formato se esta enviando la informacion
headers = {
    'content-type': 'application/json'
}
# Variable data que contiene la informacion necesaria para colocar un pedido en el servidor del restaurante
data = {
    "id":4,
    "descripcion":"quesadilla",
    "idrestaurante": 1,
    "idrepartidor":2,
    "idcliente":4,
    }

# Variable responser que realizar la accion POST al servidor restaurante para colocar el pedido
response  = requests.request("POST",urlagregar,data=json.dumps(data),headers=headers)

if response.status_code==201:
    # Pedido creado correctamente
    Log.write("Agregar Pedido\nfecha y hora: "+str(datetime.now())+' se guardo el pedido '+str(data)+"\n")
else:
    # Pedido no se pudo crear
    Log.write("fecha y hora: "+str(datetime.now())+" Error no se pudo guardar el pedido\n")
# Cierra Archivo de Logs
Log.close() 
