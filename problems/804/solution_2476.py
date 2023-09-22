def filtra_pares(a,b,c,d):
    tupla=[a,b,c,d]
    if tupla%2==0:
       return range(2,tupla+1,2)
    else:
        return range(2,tupla,2)