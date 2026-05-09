from pydantic import BaseModel

class Voto(BaseModel):
    cod_usuario: str
    cod_candidato: str