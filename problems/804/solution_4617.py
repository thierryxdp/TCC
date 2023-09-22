def filtra_pares (a,b,c,d):
    return  ((a%2) != 1,(b%2) !=1,(c%2) != 1,(d%2) !=1)
tupla = tuple(filter(par(a,b,c,d),(a,b,c,d)))
print(tupla)