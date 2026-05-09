from pydantic import BaseModel

class Candidato(BaseModel):
    cod_candidato: str
    nombre: str
    partido: str
