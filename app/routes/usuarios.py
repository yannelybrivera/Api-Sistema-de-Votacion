from fastapi import APIRouter

router = APIRouter()

@router.get("/usuarios")
def listar_usuarios():
    return {"mensaje": "Lista de usuarios"}