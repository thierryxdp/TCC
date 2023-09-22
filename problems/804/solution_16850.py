def par(x):
        return x%2 == 0
def filtra_pares (tupla):
    """dada uma tupla de 4 elemntos, retorna outra tupla apenas com os
    elementos pares da tupla original"""
    pares = ()
    if par(int(tupla[0])) == True:
        pares = tupla[0:1]
    if par(int(tupla[1])) == True:
        pares = pares + tupla[1:2]
    if par(int(tupla[2])) == True:
        pares = pares + tupla[2:3]
    if par(int(tupla[3])) == True:
        pares = pares + tupla[3:]
    return pares