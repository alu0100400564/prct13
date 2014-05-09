#!/usr/bin/python
import sys

pi = 3.1415926535897931159979634685441852

def aproximacionpi(nn):
  n=int(nn)
  suma=0
  for i in range (1,n+1):
    a = float (i-1)/n
    b = float (i)/n
    xi = ((i)-(0.5)) / float(n)
    fxi = 4.0/(1.0 + xi*xi)
    suma += fxi
  s = suma / float (n)
  return s
  
  
if __name__=="__main__":
  if (len(sys.argv)==3):
    n=int(sys.argv[1])
    veces=int(sys.argv[2])
  else:
    print "Se debe introducir el nombre del fichero mas dos numeros el primero sera el numero de intervalos y el segundo el numero de veces que se repetira. Por defecto se hara para 10 y 10"
    n = 10
    veces = 10
   
  lap = []
  le = []
  print 'Numero   Pi    Aproximacion de Pi   Error '
  for i in range (1,veces+1):
    api = aproximacionpi(n*i)
    error = (pi - api)
    lap = lap + [api]
    le = le + [error]
    print ' %2i %11.10f %11.10f %11.10f' %(i, pi, lap[i-1], le[i-1])