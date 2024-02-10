from pack1.crear_instancias import create_instance
from pack1.class_clientes import Client, Client_vip
from pack1.primera_pre_entrega import login
import json
import os

'''
client1 = Client("Francisco", "Borda", 35, "francisco@borda.com")
client2 = Client_vip("Matias", "Pisano", 35, "matias@pissano.com", "gold")
client3 = Client_vip("Nicolas", "Potrich", 35, "nicolas@potrich.com", "platinum")
'''
clients = []


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

def create_instances():
    clients_data = load_clients_from_file()
    clients = [create_instance(client_data) for client_data in clients_data]
    return clients

def start_program():

    print("""
    +-----------------------------------------+
    |Welcome, what do you want to do?         |
    +-----------------------------------------+
    | 1. Add client                           |
    | 2. Sell product                         |
    | 3. Appy discount (only for VIP persons) |
    | 4. Return product                       |
    | 5. Logout                               |
    +-----------------------------------------+
    """)


def enumerate_clients():
    """
    Display a numbered list of clients.
    """
    print("Clients:")
    for i, client in enumerate(clients):
        print(f"\t{i+1}. {client.last_name} {client.name}")


def get_client():
    """
    Prompt the user to input the index of the client and return the selected client.
    """
    try:
        client_index = int(input("Enter the index of the client: ")) - 1
        selected_client = clients[client_index]

        print('')
        print(selected_client)
        print('')
    except ValueError:
        print("\nPlease enter a valid integer for the client index.")
    except IndexError:
        print("\nThe entered index is out of range.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

    return selected_client


def add_client():
    """
    Prompt the user to input client information and add a new client to the database.
    """
    try:
        name = input('Name: ').title()
        last_name = input('Last name: ').title()
        age = input('Age: ')
        email = input('Email: ')
        
        client_json = {
            "name": name,
            "last_name": last_name,
            "age": age,
            "email": email
        }

        ruta = "/home/lordestel88/cursos/Coderhouse/Pre_entregas/Segunda_pre_entrega_Potrich/"
        db_file = os.path.join(ruta + "db.json")

        if os.path.exists(db_file):
            with open(db_file, "r") as file:
                data = json.load(file)
        else:
            data = {"clients": []}

        data["clients"].append(client_json)

        with open(db_file, "w") as file:
            json.dump(data, file, indent=4)

        print(f'The client "{last_name} {name}" was added to database.')
        print(' ')

    except ValueError:
        print("\nInvalid age. Please enter a valid integer.")
    except Exception as e:
        print(f"\nAn error occurred while adding the client: {e}")


def sell_product():
    """
    Prompt the user to select a client and sell a product to that client.
    """
    enumerate_clients()
    try:
        selected_client = get_client()
        
        product = input("Enter the product to sell: ")
        print('')
        print(selected_client.make_purchase(product))
        print('')
        
    except TypeError as e:
        print(f"\nError accessing client attributes or methods: {e}")
    except KeyboardInterrupt:
        print("\nExecution interrupted by the user.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    print('')


def apply_discount():
    """
    Prompt the user to select a client and apply a discount if the client is VIP.
    """
    enumerate_clients()
    try:
        selected_client = get_client()

        mount = int(input("How much is the purchase? "))
        print(selected_client.get_discount(mount))
        print(' ')

    except AttributeError:
        print("\nThe client isn't VIP else he doesn't have a discount.")
        print('')
    except TypeError:
        print("\nPlease enter a valid integer for the purchase amount.")
        print('')
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        print('')


def return_product():
    """
    Prompt the user to select a client and return a product.
    """
    enumerate_clients()
    try:
        selected_client = get_client()

        product = input("What product do you want to return? " )
        print(selected_client.return_product(product))
        print('')

    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


def main ():
    """
    Main function to run the program.
    """
    print("First, to start the program you must login as the root user.")
    #if login() == 'User login':
    while True:
        
        start_program()
        
        opcion = input('Option: ')
        print(' ')
        
        if opcion == '1':
            add_client()
        elif opcion == '2':
            sell_product()
        elif opcion == '3':
            apply_discount()
        elif opcion == '4':
            return_product()
        elif opcion == '5':
            print("You have been logged out. Have a great day!")
            print(' ')
            break
        else:
            print('Incorrect option.')
        
        continuar = input('Do you want to continue operating? (y/n) ').lower()
        if continuar != "y":
            break


if __name__ == "__main__":
    main()

