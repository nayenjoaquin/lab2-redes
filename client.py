#!/usr/bin/env python3
import sys
import os
import time
from tqdm import tqdm

from rudp import RUDPClient


def save_file(alldata, file_name):

    existe = os.path.exists("client-files/")
    if not existe:  # CREA LA CARPETA CLIENT FILES SI ES QUE NO EXISTE
        os.makedirs("client-files/")

    with open("client-files/" + file_name, "wb") as file:
        file.write(b"".join(alldata))
    print("\nArchivo guardado de manera correcta")


def main():
    client = RUDPClient("localhost", 10000)

    try:
        files_list = client.send_recv("get lista")
        print(f"\nArchivos disponibles:\n{files_list}")

        reply = "El archivo no existe"
        while reply == "El archivo no existe":
            file_name = input("\nIngrese el nombre del archivo: ")
            reply = client.send_recv(file_name)
            if(reply == "El archivo no existe"):
                os.system("clear")
                print("El archivo no existe, intentelo denuevo...\n")
                print(f"\nArchivos disponibles:\n{files_list}")
        n_packages, msg = reply.decode().split("<separador>")
        if msg == "ok":
            print("Solicitando archivo...")
            alldata = []
            data = ""
            print("Recibiendo archivo...")
            with tqdm(total=int(n_packages), unit="Packets") as progressbar:
                while data != "fin":
                    data = client.send_recv("dame un paquete")
                    if data != "fin":
                        alldata.append(data)
                    else:
                        save_file(alldata, file_name)
                    progressbar.update(1)
    except BaseException:
        print("no response; giving up", file=sys.stderr)

        # Necesitamos usar os._exit en lugar de sys.exit,
        # pues el proceso de esperar una respuesta del servidor
        # utiliza hilos y la salida "forzosa" que nos ofrece
        # os._exit mata esos hilos a la vez que mata el proceso
        # principal
        os._exit(1)


if __name__ == "__main__":
    main()
