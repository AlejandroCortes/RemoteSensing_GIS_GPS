# Este programa convierte coordenadas elipsoidales a Earth Centered Earth Fixed cartesian coordinates. Este programa recive como parametros la latitud, longitud, altura y los parametros a y f del elipsoide usado.

# Para convertir las coordenadas del salon de sensores remotos de WGS84 a ECEF el codigo que se debe poner en consola es python conversion.py 4.602934 -74.066425 2632 6378137 0.0033869

import sys
import math
import numpy as np

latitud1 = float(sys.argv[1]) # Parametro 1
longitud1 = float(sys.argv[2]) # Parametro 2
altura = float(sys.argv[3]) # Parametro 3

latitud = (latitud1*(math.pi))/180.0 # convertir el parametro 1 a radianes
longitud = (longitud1*(math.pi))/180.0 # convertir el parametro 2 a radianes

a = float(sys.argv[4]) # Parametro 4
f = float(sys.argv[5]) # Parametro 5



e = (2*f)-(math.pow(f,2))

N = a/(math.sqrt(1-((e)*(math.pow((math.sin(latitud)),2)))))

x = (N + altura)*(math.cos(latitud))*(math.cos(longitud))
y = (N + altura)*(math.cos(latitud))*(math.sin(longitud))
z = ((N*(1-e)) + altura)*(math.sin(latitud))

print ("\n Las coordenadas ECEF son: X = "+str(x)+" Y = "+str(y)+" Z = "+str(z)+" \n A partir de los siguientes argumentos: latitud = "+str(latitud1)+" longitud = "+str(longitud1)+" altura = "+str(altura)+" radio ecuatorial del elipsoide = "+str(a)+" flattening = "+str(f)+"\n")

