from cryptography.fernet import Fernet

def generateUniqueKey():
    key = Fernet.generate_key()
    return key