#! encoding: UTF-8
import matplotlib.pyplot as pl
import time
import timeit
import modulo

y=[]
e=[]
m=[]
a=[]
def error(nro_int,nro_test,umbral):
  fallos=0
  for i in range (nro_test):
    s=modulo.aproximacionpi(nro_int)
    error=abs(s-modulo.pi)
    if error>=umbral:
      fallos=fallos+1
  return ((fallos/nro_test)*100)

if __name__=="__main__":
   import sys
   if (len(sys.argv)==4):
     nro_int=int(sys.argv[1])
     nro_test=int(sys.argv[2])
     umbral=float(sys.argv[3])
   else:
     print "Usted debe proporcionar tres valores, errorpi.py y tres valores numéricos, ahora se ejecutará por defecto con los valores 5 5 0.1"
     nro_int=5
     nro_test=5
     umbral=0.1
     
   
   
   for i in range (nro_test):
     t=error(nro_int,nro_test,umbral)
     a=a+[t]
   print a  
   
   for i in range (1,5):
    nro_int=nro_int*i
    umbral=umbral*i
    start=time.time()
    s=error(nro_int,nro_test,umbral)
    finish=time.time()-start
    print "El porcentaje de error es de: %5.3f" %s
    print "El tiempo que tarda en realizarse es: %14.13f" %finish
    y=y+[finish]
    e=e+[nro_int]
    m=m+[umbral]
   
   
   print y
   x = [1,2,3,4]
   graf1=pl.subplot(211)
   pl.title('Tiempo')
   pl.plot(x,y, 'r-')
   pl.xlabel("Intervalos")
   pl.ylabel("Tiempo")
   
   
   
   
 
   graf2= pl.subplot(212)
   pl.title('porcentaje de fallos')
   pl.plot(e,m, 'r-')
   pl.xlabel("Error")
   pl.ylabel("Umbral")
   pl.savefig("Graficas.eps", dpi=100)
   pl.show()