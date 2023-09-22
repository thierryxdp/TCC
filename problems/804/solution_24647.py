def filtra_pares (t):
    """recebe uma tupla contendo quatro valores inteiros e retorna uma  tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam; tup->tup"""
    pares=()
    if t[0]%2==0:
        pares=pares+(t[0],)
    if t[1]%2==0:
        pares=pares+(t[1],)
    if t[2]%2==0:
        pares=pares+(t[2],)
    if t[3]%2==0:
        pares=pares+(t[3],)
    return pares