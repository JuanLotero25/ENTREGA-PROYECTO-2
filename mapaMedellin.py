import string

from direccion import direccion

def desplegar(ruta):
  archivo = open(ruta)
  texto = archivo.read()
  return texto

def obtDireccion(archivo):
  listDireccion = []
  lineas = archivo.splitlines()

  for lines in lineas:

    nombre, origen, destino, tamano, sentido, riesgocalle, geometria = lineas.splitlines()

    direcMapa = direccion()
    direcMapa.nombre(nombre)
    direcMapa.origen(origen)
    direcMapa.destino(destino)
    direcMapa.tamaño(tamano)
    direcMapa.sentido(sentido)
    direcMapa.riesgocalle(riesgocalle)
    direcMapa.geometria(geometria)
    listDireccion.append(direcMapa)
    print(lineas)

  return listDireccion

def main():
  ruta = ()
  archivo = (ruta)
