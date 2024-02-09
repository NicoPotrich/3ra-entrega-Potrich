from class_clientes import Client, Client_vip
import json
import os


def create_instance():
    path = "/home/lordestel88/cursos/Coderhouse/Pre_entregas/Segunda_pre_entrega_Potrich/"
    db_file = path + "db.json"

    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            data = json.load(file)
    else:
        data = {"clients": []}

    clients = []

    for client_data in data["clients"]:
        if "nivel" in client_data:
            client = Client_vip(
                client_data["name"],
                client_data["last_name"],
                client_data["age"],
                client_data["email"],
                client_data["level"]
            )
        else:
            client = Client(
                client_data["name"],
                client_data["last_name"],
                client_data["age"],
                client_data["email"]
            )

        clients.append(client)
    return clients

if __name__ == "__main__":
    create_instance()
