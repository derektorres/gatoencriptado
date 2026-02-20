from persistence.db import get_connection
from security.crypto import encrypt, decrypt

class User:


    def  __init__(self, id:int,name:str, account:str, password:str, curp:str):
        self.id = id
        self.name = name
        self.account = account
        self.password = password
        self.curp = curp

    def Insert(name, account, curp, password):
        connection = get_connection()
        cursor = connection.cursor()

        curp_encrypt = encrypt(curp)
        password_encrypt = encrypt(password)

        sql = "INSERT INTO users (name, account, curp, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (name, account, curp_encrypt, password_encrypt))
        connection.commit()

        cursor.close()
        connection.close()

    def get_users():
        connection = get_connection()
        cursor = connection.cursor(dictionary=True)
        sql = "SELECT id, name, curp, account, password FROM users"
        cursor.execute(sql)
        rows = cursor.fetchall()
        return[
            User(id = row["id"], name = row["name"], account = row["account"], password = decrypt(row["password"]), curp = decrypt(row["curp"]))
            for row in rows 
         ]
            
            