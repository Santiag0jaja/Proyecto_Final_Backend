""" Funciones | service """

import json
import os
from models.Voto import Voto

ARCHIVO_VOTOS = "votos.json"
CARPETA_DOCUMENTOS = "documents"


"""cargar votos a json"""
def cargar_votos():
    with open(ARCHIVO_VOTOS, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

"""guardar votos a json"""
def guardar_votos(votos):
    with open(ARCHIVO_VOTOS, "w", encoding="utf-8") as archivo:
        json.dump(votos, archivo, indent=4)

"""crear txt"""
def generar_documento(voto: Voto):
    ruta_archivo = os.path.join(CARPETA_DOCUMENTOS, f"voto_{voto.numero_id}.txt")
    with open(ruta_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(f"Nombre del votante: {voto.nombre_votante}\n")
        archivo.write(f"ID del votante: {voto.numero_id}\n")
        archivo.write(f"Voto a: {voto.voto_a}\n")

"""eliminar archivo de voto"""
def eliminar_documento(numero_id: int):
    ruta_archivo = os.path.join(CARPETA_DOCUMENTOS, f"voto_{numero_id}.txt")
    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
