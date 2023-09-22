# int,int,int,int -> tuple
def filtra_pares(a,b,c,d):
    lista = [a, b, c, d]
    if (lista[a]//2%0):
        return lista[a]
    if (lista[b]//2%0):
        return lista[b]
    if (lista[c]//2%0):
        return lista[c]
    if (lista[d]//2%0):
        return lista[d]