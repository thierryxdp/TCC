def filtra_pares(x):
    "recebe uma tupla com 4 elementos inteiros e retorna uma tupla nova com apenas os elementos pares da tupla de entrada"
    par=()
    a,b,c,d = x
    if a%2 == 0:
        par = par + (a,)
    if b%2 == 0:
        par = par +(b,)
    if c%2 == 0:
        par = par + (c,)
    if d%2 == 0:
        par = par + (d,)
    return par