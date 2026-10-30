from fastapi import FastAPI, Form, HTTPException, status
from pydantic import BaseModel
import json
try:
    with open("servidor.json", "r", encoding="utf-8") as f:
        servidor = json.load(f)
except FileNotFoundError:
    servidor = {}
    with open("servidor.json", "w", encoding="utf-8") as f:
        json.dump(servidor, f, ensure_ascii=False, indent=4)
def actualizar():
    with open("servidor.json", "w", encoding="utf-8") as f:
        json.dump(servidor, f, ensure_ascii=False, indent=4)
class User(BaseModel):
    nombre_usuario: str
    contraseña_usuario: str
    comentario: str | None = None
app = FastAPI()
@app.get("/")
def principal():
    return "no ay nada que enviar"
@app.post("/register")
def data(datos: User = Form()):
    True_datos = datos.model_dump()
    if len(True_datos["nombre_usuario"]) <= 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Por alguna razon no puso nada en su nombre"
        )
    servidor[True_datos["nombre_usuario"]] = {"contraseña":True_datos["contraseña_usuario"], "comentario":True_datos["comentario"]}
    actualizar()
    return "todo salio bien"