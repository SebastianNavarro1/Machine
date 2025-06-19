import pickle
import numpy as np

# Cargar modelo una sola vez
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

def predecir(valores: list) -> int:
    """
    Recibe lista de 4 valores [sepal_length, sepal_width, petal_length, petal_width]
    Retorna la clase predicha como int
    """
    input_array = np.array([valores])  # Convertimos a 2D
    prediccion = model.predict(input_array)
    return int(prediccion[0])
