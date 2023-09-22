def filtra_pares(t):
    """recebe uma tupla e retorna uma tupla com os elementos pares da tupla original"""
    #dessa vez sem usar lista
    vazio=()
    for x in t:
        if x%2==0:
            vazio+=(x,)
            
    return vazio