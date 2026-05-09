from fastapi import APIRouter
from app.database.connection import cursor, conexion
from app.models.voto_model import Voto 
router = APIRouter()

@router.post("/votar")
def registrar_voto(voto: Voto):
    cursor.execute("""
        SELECT * FROM votos WHERE cod_usuario = ?
    """, (voto.cod_usuario,))

    if cursor.fetchone():
        return {"mensaje": "Este usuario ya votó"}

    cursor.execute("""
        INSERT INTO votos (cod_usuario, cod_candidato)
        VALUES (?, ?)
    """, (
        voto.cod_usuario,
        voto.cod_candidato
    ))
    conexion.commit()
    return {"mensaje": "Voto registrado correctamente"}