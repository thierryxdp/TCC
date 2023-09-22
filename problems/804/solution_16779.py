#Start your python function here
import math
def filtra_pares(x):
    a= int(x[0])
    b= int(x[1])
    c= int(x[2])
    d= int(x[3])
    e= (a,b,c,d)
    f= ()
    if math.floor(a%2)==0:
       return [a]+f()
    elif math.floor(b%2)==0:
         return [b]+f()
    elif math.floor(c%2)==0:
         return [c]+f()
    elif math.floor(d%2)==0:
         return [d]+f()
    else:
          return ()