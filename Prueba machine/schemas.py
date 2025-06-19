from pydantic import BaseModel
from typing import List

class IrisInput(BaseModel):
    valores: List[float]  # 4 valores para el modelo Iris
