## Estructura de la API

Este código provee las siguientes clases:

- `RUDPServer(port)`: crea un servidor UDP fiable en el puerto `port`.
    - `receive()`: Espera a recibir un mensaje de algún cliente, retornando su contenido y su dirección de origen.
    - `reply(address, payload)`: Envía `payload` al cliente en `address`.
- `RUDPClient(address, port)`: crea un cliente UDP fiable que se conecta al servidor en `address`:`port`.
    - `send_recv(payload)`: Envía `payload` al servidor y reintenta un determinado número de veces hasta obtener una respuesta

Les recomiendo mirar los ejemplos en `server.py` y `client.py` para entender cómo utilizar estas clases.


## EJECUCIÓN DEL PROGRAMA

Para ejecutar el programa primero instalar pip y ejecutar el sgte comando

  ~$ pip install -r requirements.txt

Luego ejecutar el servidor 

  ~$ python server.py

Los archivos que desea disponer para su descarga deben estar en la carpeta server-files

Luego ejecutamos el cliente

  ~$ python client.py

Dentro de la ejecución del cliente debera elegir el archivo a descargar y este se guardara en la carpeta
client-files (será creada si no existe).

El código fue procesado con autopep8.