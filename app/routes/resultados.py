from fastapi import APIRouter
from app.database.connection import cursor

router = APIRouter()

@router.get("/resultados")
def ver_resultados():
    cursor.execute("""
            SELECT
            c.NOMBRE_CANDIDATO,
            c.PARTIDO_POLITICO,
            COUNT(v.CANDIDATO_ID) AS total_votos
        FROM TB_CANDIDATO c
        LEFT JOIN TB_VOTO v ON c.ID_CANDIDATO = v.CANDIDATO_ID
        GROUP BY c.NOMBRE_CANDIDATO, c.PARTIDO_POLITICO
        ORDER BY total_votos DESC
        """)
    columnas = [col[0] for col in cursor.description]
    filas = cursor.fetchall()
    return [dict(zip(columnas, fila)) for fila in filas]

@router.get("/resultados/ganador")
def ver_ganador():
    cursor.execute("""
        SELECT TOP 1
            c.NOMBRE_CANDIDATO,
            c.PARTIDO_POLITICO,
            COUNT(v.CANDIDATO_ID) AS total_votos
        FROM TB_CANDIDATO c
        LEFT JOIN TB_VOTO v ON c.ID_CANDIDATO = v.CANDIDATO_ID
        GROUP BY c.NOMBRE_CANDIDATO, c.PARTIDO_POLITICO
        ORDER BY total_votos DESC
    """)
    columnas = [col[0] for col in cursor.description]
    fila = cursor.fetchone()
    if not fila:
        return {"mensaje": "No hay votos aún"}
    return dict(zip(columnas, fila))