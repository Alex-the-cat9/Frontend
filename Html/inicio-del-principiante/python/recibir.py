from fastapi import FastAPI, Form
from pydantic import BaseModel
app = FastAPI()
class Datos_user(BaseModel):
    usuario_nombre: str
    usuario_contraseña: str
@app.get("/")
def entrar():
    print("Usuario desconocido entro ala api")
    return "Registrate"
@app.post("/registro")
def registro(datos: Datos_user = Form()):
    datos_usuario = datos.model_dump()
    print("los datos del html ya llegaron")
    print(datos_usuario)
    return {
        "proceso":"exito",
        "datos":datos_usuario
    }