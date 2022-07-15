#!/usr/bin/env python3

from importlib.resources import path
from rudp import RUDPServer
import os
import threading

size = 8000


def send_file(file_name, server, address):
    print(f"Enviando archivo '{file_name}'...")
    with open("server-files/" + file_name, "rb") as f:
        while True:
            data = f.read(size)
            if not data:
                server.reply(address, "fin")
                break
            msg_aux, add_aux = server.receive()
            server.reply(address, data)

    os._exit(1)


def app(server, address):

    files_list = os.listdir("server-files")
    files_list = "\n* ".join(files_list)
    files_list = f"* {files_list}"
    server.reply(address, files_list)

    while True:
        message, address = server.receive()

        if message != "dame un paquete":
            if message in os.listdir("server-files"):
                print(f"{address}: Nueva solicitud '{message}'...")
                file_size = os.path.getsize(
                    "server-files/" + message) // size + 1
                msg = f"{file_size}<separador>ok"
                server.reply(address, msg.encode())
                send_file(message, server, address)
            else:
                server.reply(address, "El archivo no existe")


def main():
    server = RUDPServer(10000)
    while True:
        message, address = server.receive()
        if message == "get lista":
            # Intento de multi threading
            # print("new thread")
            # thread = threading.Thread(target=app, args=(server,address))
            # thread.start()
            app(server, address)


if __name__ == "__main__":
    main()
