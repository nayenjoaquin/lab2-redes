#!/usr/bin/env python3
import sys
import os
import time

from rudp import RUDPClient


def save_file(reply, file_name):
    with open("client-files/"+file_name, "wb") as f:
        f.write(reply)

def main():
    client = RUDPClient("localhost", 10000)


    connection = True
    while connection:
        try:
            reply = client.send_recv(b"NPC - MIRAME.wav")
            save_file(reply, "archivo.txt")
            connection = False
        except:
            print("no response; giving up", file=sys.stderr)

            # Necesitamos usar os._exit en lugar de sys.exit,
            # pues el proceso de esperar una respuesta del servidor
            # utiliza hilos y la salida "forzosa" que nos ofrece
            # os._exit mata esos hilos a la vez que mata el proceso
            # principal
            os._exit(1)

        time.sleep(10)


if __name__ == "__main__":
    main()
