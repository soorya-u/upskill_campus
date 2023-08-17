import hashlib

def creatingHash(password):
    password_hash=hashlib.sha512(password.encode()).hexdigest()
    return password_hash