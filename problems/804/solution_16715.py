#Start your python function here
import math
def filtra_pares(x):
    a= x[0]
    b= x[1]
    c= x[2]
    d= x[3]
    return[filtro(a),filtro(b),filtro(c),filtro(d)]
def filtro(x):
    if math.ceil(x%2)==0:
        return[x]
    else:
         return[]