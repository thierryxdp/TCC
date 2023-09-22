def par(n):
    'retorna true se n for par; float->bool'
    return n%2==0
def filtra_pares(t):
    'retorna a ordenação dos elementos de uma tupla em pares uma nova dupla contendo somente os pares da antiga'
    pares=()
    if par(t[0]):
        pares = pares + (t[0],)
    if par(t[1]):
        pares = pares + (t[1],)
    if par(t[2]):
        pares = pares + (t[2],)
    if par(t[3]):
        pares = pares + (t[3],)
    return pares