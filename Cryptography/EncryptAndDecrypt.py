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