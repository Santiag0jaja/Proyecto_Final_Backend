from pydantic import BaseModel

class Voto(BaseModel):
    nombre_votante: str
    numero_id: int
    voto_a: str
