def par(x):
    """Funcao que retonar True se o numero for par e False caso nao seja
    float -> bool"""
    return x/2==0
def filtra_pares(y):
    """Funcao que recebe uma tupla de 4 valores e devolve uma tupla com apenas os valores pares
    tup -> tup"""
    pares=()
    
    if par(x[0]):
        pares= pares+(x[0],)
    if par(x[1]):
        pares=pares+(x[1],)
    if par(x[2]):
        pares=pares+(x[2],)
    if par(x[3]):
        pares=pares+(x[3],)
    return pares