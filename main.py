""" Main code | Proyecto Final: Votaciones"""

from fastapi import FastAPI, HTTPException
from models.Voto import Voto
from service.voto_service import (
    cargar_votos, guardar_votos, generar_documento, eliminar_documento
)

app = FastAPI()

"""Registrar y crear voto"""
@app.post("/votos")
def registrar_voto(voto: Voto):
    votos = cargar_votos()
    
    if str(voto.numero_id) in votos:
        raise HTTPException(status_code=400, detail="El voto ya existe")
    
    votos[str(voto.numero_id)] = voto.dict()
    guardar_votos(votos)
    generar_documento(voto)

    return {"mensaje": "Voto registrado", "voto": voto}

"""Devolver voto por id"""
@app.get("/votos/{numero_id}")
def obtener_voto(numero_id: int):
    votos = cargar_votos()
    
    if str(numero_id) not in votos:
        raise HTTPException(status_code=404, detail="Voto no encontrado")
    
    return votos[str(numero_id)]

"""actualizar voto"""
@app.put("/votos/{numero_id}")
def actualizar_voto(numero_id: int, voto_actualizado: Voto):
    votos = cargar_votos()
    
    if str(numero_id) not in votos:
        raise HTTPException(status_code=404, detail="Voto no encontrado")
    
    votos[str(numero_id)] = voto_actualizado.dict()
    guardar_votos(votos)
    generar_documento(voto_actualizado)

    return {"mensaje": "Voto actualizado", "voto": voto_actualizado}

"""Eliminar voto"""
@app.delete("/votos/{numero_id}")
def eliminar_voto(numero_id: int):
    votos = cargar_votos()
    
    if str(numero_id) not in votos:
        raise HTTPException(status_code=404, detail="Voto no encontrado")
    
    del votos[str(numero_id)]
    guardar_votos(votos)
    eliminar_documento(numero_id)

    return {"mensaje": "Voto eliminado"}
