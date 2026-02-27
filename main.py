from entities.user import User
from getpass import getpass

def register_user():
    name = input("nombre: ")
    account = input("cuenta: ")

    if User.check_account_exists(account):
        print("La cuenta ya existe")
    else:
        curp = input("CURP: ")
        password = getpass("Contraseña: ")

        User.Insert(name, account, curp, password)

def view_users():
    users = User.get_users()
    for user in users:
        print(f""" ID: {user.id} Nombre: {user.name} Cuenta: {user.account} CURP: {user.curp} contraseña: {user.password}""")
    
def login():
    account = input("cuenta: ")
    password = getpass("Contraseña: ")

    user = User.get_user_by_account(account)
        
    if user and user.password == password:
        return user
    else:
        return None
    #return if user adn user.password == pasword

def add_card(id_usuario):
    numero_tarjeta = getpass("ingresa el numero de la tarjeta: ")
    banco = input("Banco: ")
    tipo_tarjeta = input("Tipo de tarjeta: ")
    User.add_card(numero_tarjeta, banco, tipo_tarjeta, id_usuario)



if __name__ == "__main__":
    print("INICIO DE SESION")
    usuario = login()
    if usuario:

        print("seleccione una opcion del menu")
        print("1.- registrar un usuario")
        print("2.-consultar usuarios")
        print("3.- agregar tarjetaaa")
        option = int(input())
        if option == 1:
            register_user()
        elif option == 2:
            view_users()
        elif option == 3:
            add_card(usuario.id)
    else:
        print("nomas nada wei")
