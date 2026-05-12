from fastapi import FastAPI
from app.routes import usuarios, candidatos, votos

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(candidatos.router)
app.include_router(votos.router)


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}