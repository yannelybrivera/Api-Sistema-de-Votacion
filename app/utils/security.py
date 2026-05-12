import bcrypt

def encriptar_password(password: str) -> str:
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(password_bytes, salt)
    return hash.decode('utf-8')

def verificar_password(password: str, hash: str) -> bool:
    password_bytes = password.encode('utf-8')
    hash_bytes = hash.encode('utf-8')
    return bcrypt.checkpw(password_bytes, hash_bytes)