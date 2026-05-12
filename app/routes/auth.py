from fastapi import APIRouter
from app.database.connection import cursor
from app.models.usuario_model import Usuario
from app.utils.security import verificar_password
from app.utils.jwt import crear_token
from pydantic import BaseModel

router = APIRouter()

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(datos: LoginRequest):
    cursor.execute("""
                SELECT COD_USUARIO, NOMBRE_USUARIO, PASSWORD_HASH
                FROM TB_USUARIO
                WHERE EMAIL = ? AND ESTADO = 1
                """, (datos.email,))
    
    usuario = cursor.fetchone()
    
    if not usuario:
        return {"error": "Usuario no encontrado"}
    
    cod_usuario = usuario[0]
    nombre = usuario[1]
    password_hash = usuario[2]

    if not verificar_password(datos.password, password_hash):
        return {"error": "Contraseña incorrecta"}
    
    
    token = crear_token({"sub": cod_usuario, "nombre": nombre})
    
    return {
        "mensaje": "Login exitoso",
        "token": token,
        "nombre": nombre
    }