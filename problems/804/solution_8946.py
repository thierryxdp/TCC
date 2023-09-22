def fitra_pares(x,y,z,w):
    """dada uma tupla com quatro numeros inteiros, retorna os pares
    int,int,int,int-tuple"""
    pares=()
    if x%2 == 0:
        pares = pares + (t[0],)
    if y%2 == 0:
        pares = pares + (t[1],)
    if z%2 == 0:
        pares = pares + (t[2],)
    if w%2 == 0:
        pares = pares + (t[3],)
    return pares