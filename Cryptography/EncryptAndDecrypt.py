from cryptography.fernet import Fernet

key = None

def generateUniqueKey():
    global key
    key = Fernet.generate_key()