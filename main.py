from entities.user import User
from getpass import getpass

def register_user():
    name = input("nombre: ")
    account = input("cuenta: ")
    curp = input("CURP: ")
    password = getpass("Contraseña: ")

    User.Insert(name, account, curp, password)

def view_users():
    users = User.get_users()
    for user in users:
        print(f""" ID: {user.id} Nombre: {user.name} Cuenta: {user.account} CURP: {user.curp} contraseña: {user.password}""")
    

if __name__ == "__main__":
    print("seleccione una opcion del menu")
    print("1.- registrar un usuario")
    print("2.-consultar usuarios")
    option = int(input())
    if option == 1:
        register_user()
    elif option == 2:
        view_users()
