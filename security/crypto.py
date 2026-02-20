from cryptography.fernet import Fernet

key = b'dx2t6h4llSEN6I5CwucgB9ojKmHokmP8wYe2T45E7qQ='
fernet = Fernet(key)
def encrypt(value):
    return fernet.encrypt(value.encode()).decode()

def decrypt(value):
    return fernet.decrypt(value.encode()).decode()