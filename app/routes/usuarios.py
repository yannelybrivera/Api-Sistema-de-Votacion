from fastapi import APIRouter
from app.database.connection import cursor, conexion
from app.models.usuario_model import Usuario
from app.utils.security import encriptar_password

router = APIRouter()

@router.get("/usuarios")
def listar_usuarios():
    cursor.execute("SELECT * FROM TB_USUARIO")
    columnas = [col[0] for col in cursor.description]  
    filas = cursor.fetchall()
    return [dict(zip(columnas, fila)) for fila in filas]

@router.post("/usuarios")
def crear_usuario(usuario: Usuario):
    
    password_encriptado = encriptar_password(usuario.password_hash)
    
    cursor.execute("""
        INSERT INTO TB_USUARIO (cod_usuario, nombre_usuario, email, password_hash)
        VALUES (?, ?, ?, ?)
    """, (
        usuario.cod_usuario,
        usuario.nombre_usuario,
        usuario.email,
        password_encriptado
    ))
    conexion.commit()
    return {"mensaje": "Usuario creado correctamente"}