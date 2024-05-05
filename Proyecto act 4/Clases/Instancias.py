from Clases.ClasesGenerales import *


portero1 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'ptad.png')
portero2 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'pcurl.png')
portero3 = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'padel.png')

TadJ = Portero("Tad", portero1)
CurlJ = Portero("Curl", portero2)
AdelJ = Portero("Adel", portero3)

portero1rv = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'pmarc.png')
portero2rv = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'plui.png')
portero3rv = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'pBati.png')

marcrv = Portero("Marc", portero1rv)
luirv = Portero("Lui", portero2rv)
batirv = Portero("Bati", portero3rv)

portero1m = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'pito.png')
portero2m = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'prigo.png')
portero3m = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'pcris.png')

Itom = Portero("Ito", portero1m)
Rigom = Portero("Rigo", portero2m)
Crism = Portero("Cris", portero3m)


###Artilleros


artillero1juv = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'dan.png')
artillero2juv = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'mia.png')
artillero3juv = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'Ava.png')

Dan = Artillero("Dan", artillero1juv)
mia = Artillero("Leo", artillero2juv)
Ava = Artillero("Sam", artillero3juv)

artillero1m = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'Max.png')
artillero2m = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'leo.png')
artillero3m = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'sam.png')

Max = Artillero("Max", artillero1m)
leo = Artillero("Leo", artillero2m)
sam = Artillero("Sam", artillero3m)

artillero1rv = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'lily.png')
artillero2rv = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'ben.png')
artillero3rv = os.path.join(os.path.dirname(__file__), '..', 'Imagenes', 'alex.png')

lily = Artillero("Lily", artillero1rv)
Ben = Artillero("Ben", artillero2rv)
Alex = Artillero("Alex", artillero3rv)



###Escudos
Escudo_MIL = os.path.join(os.path.dirname(__file__),'..', 'Imagenes', 'emil.png')
Escudo_JUV = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'ejuv.png')
Escudo_RIV = os.path.join(os.path.dirname(__file__), '..',  'Imagenes', 'erp.png')

MIL = Equipo("Milan", Escudo_MIL, [], [], [])
JUV = Equipo("Juventus", Escudo_JUV, [], [], [])
RIV = Equipo("River Plate", Escudo_RIV, [], [], [])


