from cryptography.fernet import Fernet

key = None

def generateUniqueKey():
    global key
    key = Fernet.generate_key()

def getUniqueKey():
    global key
    if key is not None:
        return key
    
def destroyUniqueKey():
    global key
    if key is not None:
        key = None

def Encrypt(string,key):
    if key is not None:
        string_bytes = bytes(string,'utf-8')
        return Fernet(key).encrypt(string_bytes)
    
def Decrypt(string_byte,key):
    if key is not None:
        string = Fernet(key).decrypt(string_byte).decode()
        return string