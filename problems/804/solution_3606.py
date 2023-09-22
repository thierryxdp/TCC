# int,int,int,int -> tuple
def filtra_pares(a,b,c,d):
    lista = [a, b, c, d]
    if (lista[a]//2%0):
        return lista[a]
    elif (lista[b]//2%0):
        return lista[b]
    elif (lista[c]//2%0):
        return lista[c]
    elif (lista[d]//2%0):
        return lista[d]