from pydantic import BaseModel

class Usuario(BaseModel):
    cod_usuario: str
    nombre_usuario: str
    email: str
    password_hash: str

