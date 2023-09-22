"""dada a os dados retorna uma nova dupla contendo os elementos pares da tupla original"""
import math
def filtra_pares (num):
    r=[]
    for n in num:
        if n%2==0:
            r.append (n)
    r=tuple (r)
    print (r)
    return(r)