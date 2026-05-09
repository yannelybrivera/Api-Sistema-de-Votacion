from fastapi import APIRouter
from app.database.connection import cursor, conexion
from app.models.candidato_model import Candidato  

router = APIRouter()

@router.get("/candidatos")
def listar_candidatos():
    cursor.execute("SELECT * FROM candidatos")
    columnas = [col[0] for col in cursor.description] 
    filas = cursor.fetchall()
    return [dict(zip(columnas, fila)) for fila in filas]

@router.post("/candidatos")
def crear_candidato(candidato: Candidato):
    cursor.execute("""
        INSERT INTO candidatos (cod_candidato, nombre, partido)
        VALUES (?, ?, ?)
    """, (
        candidato.cod_candidato,
        candidato.nombre,
        candidato.partido
    ))
    conexion.commit()
    return {"mensaje": "Candidato creado correctamente"}