import hashlib

def creatingHash(password):
    password_hash=hashlib.sha512(password.encode()).hexdigest()
    return password_hash

def verifyingHash(password,stored_password_hash):

    password_hash=hashlib.sha512(password.encode()).hexdigest()
    if(password_hash==stored_password_hash):
        return True
    return False

def generatePassword():
    pass