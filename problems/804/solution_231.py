# Filtragem.
def filtra_pares(t):
    '''Essa função recebe uma tupla de quatro elementos e filtra os pares, retornando outra tupla;
    TUPLA -> TUPLA'''
    tr = ()
    if t[0]%2 == 0:
        tr = tr + (t[0],)
    if t[1]%2 == 0:
        tr = tr + (t[1],)
    if t[2]%2 == 0:
        tr = tr + (t[2],)
    if t[3]%2 == 0:
        tr = tr + (t[3],)
    return tr