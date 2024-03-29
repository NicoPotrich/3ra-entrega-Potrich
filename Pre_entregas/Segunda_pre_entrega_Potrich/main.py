from pack1.class_clientes import Client, Client_vip
from pack1.primera_pre_entrega import login
import json
import os


def load_clients_from_file():
    """
    Load client data from the JSON file.
    
    Returns:
        list: List of client data dictionaries.
    """
    path = "/home/lordestel88/cursos/Coderhouse/Pre_entregas/Segunda_pre_entrega_Potrich/"
    db_file = os.path.join(path, "db.json")

    if os.path.exists(db_file):
        with open(db_file, "r") as file:
            data = json.load(file)
            clients_data = data.get("clients", [])
    else:
        clients_data = []
    
    return clients_data

def save_clients_to_file(clients_data):
    """
    Save client data to the JSON file.
    
    Args:
        clients_data (list): List of client data dictionaries.
    """
    path = "/home/lordestel88/cursos/Coderhouse/Pre_entregas/Segunda_pre_entrega_Potrich/"
    db_file = os.path.join(path, "db.json")

    with open(db_file, "w") as file:
        json.dump({"clients": clients_data}, file, indent=4)

def create_instance(client_data):
    """
    Create a client instance from the provided data.
    
    Args:
        client_data (dict): Dictionary containing client data.
        
    Returns:
        Client: Instance of Client or Client_vip class.
    """
    if client_data["level"] == "gold" or client_data["level"] == "platinum":
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
    return client

def create_instances():
    """
    Create instances of clients from the data loaded from the file.
    
    Returns:
        list: List of client instances.
    """
    clients_data = load_clients_from_file()
    clients = [create_instance(client_data) for client_data in clients_data]
    return clients

def start_program():
    """
    Display the main menu of the program.
    """
    print("""
    +-----------------------------------------+
    |Welcome, what do you want to do?         |
    +-----------------------------------------+
    | 1. Add client                           |
    | 2. Lists clients                        |
    | 3. Delete client                        |
    | 4. Sell product                         |
    | 5. Appy discount (only for VIP persons) |
    | 6. Return product                       |
    | 7. Logout                               |
    +-----------------------------------------+
    """)

def list_clients():
    """
    List all the clients.
    """
    clients = create_instances()
    print("Clients:")
    for i, client in enumerate(clients):
        print(f"\t{i+1}. {client.last_name} {client.name}")
    print("")

def get_client():
    """
    Prompt the user to select a client and return the selected client instance.
    """
    try:
        client_index = int(input("Enter the index of the client: ")) - 1
        clients = create_instances()

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
        level = input('Level (regular/gold/platinum): ')
        
        client_data = {
            "name": name,
            "last_name": last_name,
            "age": age,
            "email": email,
            "level": level
        }

        clients_data = load_clients_from_file()
        clients_data.append(client_data)
        save_clients_to_file(clients_data)

        print(f'The client "{last_name} {name}" was added to database.')
        print(' ')

        create_instances()

    except ValueError:
        print("\nInvalid age. Please enter a valid integer.")
    except Exception as e:
        print(f"\nAn error occurred while adding the client: {e}")

def get_client_index():
    """
    Prompt the user to input the index of the client and return the selected index.
    """
    try:
        client_index = int(input("Enter the index of the client: ")) - 1
        return client_index
    except ValueError:
        print("\nPlease enter a valid integer for the client index.")
        return None

def del_client():
    """
    Prompt the user to select a client to delete from the database.

    This function lists all the clients, prompts the user to select a client
    by index, confirms the deletion, and then deletes the selected client from
    the database file.
    """
    try:
        list_clients()
        client_index = get_client_index()

        if client_index is None:
            return

        clients_data = load_clients_from_file()

        confirm = input("Are you sure you want to delete this client? (y/n): ").lower()
        if confirm != "y":
            print("Deletion canceled.")
            print("")
            return

        del clients_data[client_index]

        save_clients_to_file(clients_data)
        
        print("Client successfully deleted.")
        print("")

    except Exception as e:
        print(f"An error occurred: {e}")

def sell_product():
    """
    Prompt the user to select a client and sell a product to that client.
    """
    list_clients()
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
    list_clients()
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
    list_clients()
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
    if login() == 'User login':
        create_instances()

        while True:
            
            start_program()
            
            opcion = input('Option: ')
            print("")
            
            if opcion == '1':
                add_client()
            elif opcion == '2':
                list_clients()
            elif opcion == '3':
                del_client()
            elif opcion == '4':
                sell_product()
            elif opcion == '5':
                apply_discount()
            elif opcion == '6':
                return_product()
            elif opcion == '7':
                print("You have been logged out. Have a great day!")
                print("")
                break
            else:
                print('Incorrect option.')
                print("")
            
            continuar = input('Do you want to continue operating? (y/n) ').lower()
            if continuar != "y":
                print("")
                print("You have been logged out. Have a great day!")
                print("")
                break

if __name__ == "__main__":
    main()

