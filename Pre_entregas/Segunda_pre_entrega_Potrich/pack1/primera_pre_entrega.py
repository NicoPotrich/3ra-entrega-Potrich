import json

users = {"root": "123"}

def inicio_programa():
    '''
    Display the main menu of the program.
    '''
    print("""
    +---------------------------------+
    |Welcome, what do you want to do? |
    +---------------------------------+
    | 1. Add User                     |
    | 2. Show Users                   |
    | 3. Save Data                    |
    | 4. Logout                       |
    +---------------------------------+
    """)


def login():
    """
    Prompt the user for their username and password and perform login authentication.
    """
    login_user = input('User: ')
    if login_user not in users:
        print("Username doesn't exist\n")
    else:
        for intentos in range(3):
            password = input('Password: ')
            if users[login_user] == password:
                return 'User login'
            else:
                print(f'Incorrect password. {2-intentos} attempts left\n')


def agregar_usuario():
    """
    Prompt the user to add a new username and password.
    """
    new_user = input('Username (must contain at least 6 characters): ')
    
    while len(new_user) < 6:
        print('**Incorrect user**\n')
        new_user = input('Username (must contain at least 6 characters): ')
    if new_user in users:
        print('User already exists')
    else:
        password = input('Password (must contain at least 6 characters): ')
        while len(password) < 6:
            print('**Password incorrect**\n')
            password = input('Password (must contain at least 6 characters): ')
        users[new_user] = password
        print(f'The user "{new_user}" was added.')
        print(' ')


def mostrar_usuarios():
    """
    Display the list of users and their passwords.
    """
    print('Users list:')
    if len(users) == 0:
        print('\t', None)
    else:
        for i, (key, value) in enumerate(users.items(), start=1):
            print(f'\t{i}. {key}: {value}')
    print (' ')


def guardar_usuarios(users):
    """
    Save the user data to a JSON file.
    """
    ruta = "Coderhouse/Pre_entregas/"
    with open(ruta+r"DB.txt", "w") as file:
        json.dump(users, file, indent=4)
    print("Data saved in the database")


def main ():
    """
    Main function to run the program.
    """
    print("To start the program you must login as the root user.")
    if login() == 'User login':
        while True:
            
            inicio_programa()
            
            opcion = input('Option: ')
            print(' ')
            
            if opcion == '1':
                agregar_usuario()
            elif opcion == '2':
                mostrar_usuarios()
            elif opcion == '3':
                guardar_usuarios(users)
            elif opcion == '4':
                print("You have been logged out. Have a great day!")
                break
            else:
                print('Incorrect option.')
            
            continuar = input('Do you want to continue operating? (y/n) ').lower()
            if continuar != "y":
                break


if __name__ == "__main__":
    main()


    