#!/usr/bin/env python3

from importlib.resources import path
from rudp import RUDPServer
import os

size = 1024

def send_file(file_name,server,address):
   
    with open ("server-files/"+file_name, "rb") as f:
        while True:
            data = f.read(1024)
            if not data:
                break
            server.reply(address,data)

def main():
    server = RUDPServer(10000)

    while True:
        message, address = server.receive()
        message = message.decode("utf-8")
        print(f"{address}: Solicitando archivo {message}...")

        # Enviar archivo o mensaje de error
        send_file(message,server,address)


if __name__ == "__main__":
    main()
