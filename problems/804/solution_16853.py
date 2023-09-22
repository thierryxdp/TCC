def par(x):
        return x%2 == 0
def filtra_pares (tupla):
    """dada uma tupla de 4 elemntos, retorna outra tupla apenas com os
    elementos pares da tupla original"""
    if type(tupla) != tuple:
        tup = tuple(tupla)
        else:
            tup = tupla
    pares = ()
    if par(tup[0]) == True:
        pares = () + tup[0:1]
    if par(tup[1]) == True:
        pares = pares + tup[1:2]
    if par(tup[2]) == True:
        pares = pares + tup[2:3]
    if par(tup[3]) == True:
        pares = pares + tup[3:]
    return pares