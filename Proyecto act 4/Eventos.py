import random
from Clases.Instancias import *
equipos = [MIL, JUV, RIV]#instyancias
porteros = [TadJ, CurlJ, AdelJ]
porteros2 = [marcrv, luirv, batirv]
porteros3 = [Itom, Rigom, Crism]
artilleros = [Dan, mia, Ava]
artilleros2 = [lily, Ben, Alex]
artilleros3 = [Max, leo, sam]
Visloclista = [1,2]
resul = []
equipo_seleccionado = random.choice(equipos)

def guardar_equipo_1(equipo="", artillero= "", portero="", resul= ""):
    with open('equipo_1.txt', 'w') as archivo:
        archivo.write(f"Nombre: {equipo}, ")
        archivo.write(f"Portero: {portero}, ")
        archivo.write(f"Artillero: {artillero}, ")
        archivo.write(f"VisLoc: {resul} ")
        print("Guardado")

def guardar_equipo_2(equipo="", artillero= "", portero="", resul= ""):
    with open('equipo_2.txt', 'w') as archivo:
        archivo.write(f"Nombre: {equipo}, ")
        archivo.write(f"Portero: {portero}, ")
        archivo.write(f"Artillero: {artillero}, ")
        archivo.write(f"VisLoc: {resul} ")
        print("Guardado")

def all1():
    global resul
    global equipo_seleccionado
    if equipo_seleccionado == MIL:
        artilleros_sele1 = random.choice(artilleros3)
        porteros_sele1 = random.choice(porteros3)
        Visloc = random.choice(Visloclista)
        if Visloc == 1:
            resul = "Local"
        elif Visloc == 2:
            resul = "Visitante"
    if equipo_seleccionado == JUV:
        artilleros_sele1 = random.choice(artilleros)
        porteros_sele1 = random.choice(porteros)
        Visloc = random.choice(Visloclista)
        if Visloc == 1:
            resul = "Local"
        elif Visloc == 2:
            resul = "Visitante"
    if equipo_seleccionado == RIV:
        artilleros_sele1 = random.choice(artilleros2)
        porteros_sele1 = random.choice(porteros2)
        Visloc = random.choice(Visloclista)
        if Visloc == 1:
            resul = "Local"
        elif Visloc == 2:
            resul = "Visitante"

    return guardar_equipo_1(equipo_seleccionado.nombre, artilleros_sele1.nombre, porteros_sele1.nombre, resul)
    
def all2(equipo_seleccionado):
    global resul
    resul2 = ""
    if resul == "Local":
            resul2 = "Visitante"
    elif resul == "Visitante":
            resul2 = "Local"
    if equipo_seleccionado == MIL:
        equipo_seleccionado2 = random.choice([JUV, RIV])
        if equipo_seleccionado2 == JUV:
            artilleros_sele2 = random.choice(artilleros)
            porteros_sele2 = random.choice(porteros)
        if equipo_seleccionado2 == RIV:
            artilleros_sele2 = random.choice(artilleros2)
            porteros_sele2 = random.choice(porteros2)

    if equipo_seleccionado == JUV:
        equipo_seleccionado2 = random.choice([MIL, RIV])
        if equipo_seleccionado2 == MIL:
            artilleros_sele2 = random.choice(artilleros3)
            porteros_sele2 = random.choice(porteros3)
        if equipo_seleccionado2 == RIV:
            artilleros_sele2 = random.choice(artilleros2)
            porteros_sele2 = random.choice(porteros2)
    
    if equipo_seleccionado == RIV:
        equipo_seleccionado2 = random.choice([MIL, RIV])
        if equipo_seleccionado2 == MIL:
            artilleros_sele2 = random.choice(artilleros3)
            porteros_sele2 = random.choice(porteros3)
        if equipo_seleccionado2 == JUV:
            artilleros_sele2 = random.choice(artilleros)
            porteros_sele2 = random.choice(porteros)

    return guardar_equipo_2(equipo_seleccionado2.nombre, artilleros_sele2.nombre, porteros_sele2.nombre, resul2)

