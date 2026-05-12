from fastapi import APIRouter
from app.database.connection import cursor, conexion
from app.models.voto_model import Voto 
router = APIRouter()

@router.post("/votar")
def registrar_voto(voto: Voto):
    cursor.execute("""
        SELECT * FROM TB_VOTO WHERE USUARIO_ID = ?
    """, (voto.cod_usuario,))

    if cursor.fetchone():
        return {"mensaje": "Este usuario ya votó"}

    cursor.execute("SELECT COUNT(*) FROM TB_VOTO")
    conteo = cursor.fetchone()[0]
    id_voto = f"V{str(conteo + 1).zfill(7)}"

    cursor.execute("""
        INSERT INTO TB_VOTO (ID_VOTO, USUARIO_ID, CANDIDATO_ID, FECHA_VOTO)
        VALUES (?, ?, ?, ?)
    """, (
        id_voto,
        voto.cod_usuario,
        voto.cod_candidato,
        datetime.now()
    ))
    conexion.commit()
    return {"mensaje": "Voto registrado correctamente"}