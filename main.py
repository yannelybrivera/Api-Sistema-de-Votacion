from fastapi import FastAPI
from app.routes import usuarios, candidatos, votos, auth, resultados

app = FastAPI()

app.include_router(usuarios.router)
app.include_router(candidatos.router)
app.include_router(votos.router)
app.include_router(auth.router)
app.include_router(resultados.router)


@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}