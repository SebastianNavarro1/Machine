from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from model.predictor import predecir
from schemas import IrisInput

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def inicio():
    return {"mensaje": "API FastAPI para modelo Iris"}

@app.post("/predict")
def predict_iris(data: IrisInput):
    resultado = predecir(data.valores)
    nombre = ["Setosa", "Versicolor", "Virginica"][resultado] if resultado in [0, 1, 2] else "Desconocida"
    return {"clase_predicha": resultado, "nombre_clase": nombre}

@app.get("/formulario", response_class=HTMLResponse)
def mostrar_formulario(request: Request):
    return templates.TemplateResponse("formulario.html", {"request": request})

