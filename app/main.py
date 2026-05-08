from fastapi import FastAPI
from app.routes import usuarios

app = FastAPI()

app.include_router(usuarios.router)

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}