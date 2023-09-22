# Filtra a tupla t e retorna seus elementos pares
# tuple -> tuple
def filtra_pares(t):
    tuplaPares = ()

    if(t[0] % 2 == 0):
        tuplaPares = (t[0],)

    if(t[1] % 2 == 0):
        tuplaPares += (t[1],)

    if(t[2] % 2 == 0):
        tuplaPares += (t[2],)

    if(t[3] % 2 == 0):
        tuplaPares += (t[3],)

    return tuplaPares