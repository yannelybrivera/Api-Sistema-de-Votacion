from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "clave_super_secreta_123"
ALGORITHM = "HS256"
EXPIRE_MINUTOS = 60

def crear_token(data: dict) -> str:
    datos = data.copy()
    expiracion = datetime.utcnow() + timedelta(minutes=EXPIRE_MINUTOS)
    datos.update({"exp": expiracion})
    token = jwt.encode(datos, SECRET_KEY, algorithm =ALGORITHM)
    return token

def verificar_token(token: str) -> dict:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None