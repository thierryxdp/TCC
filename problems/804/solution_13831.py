def filtra_pares(t):
    """recebe uma tupla com 4 elementos inteiros como 
    parâmetro e retorna uma nova tupla contendo apenas os
    elementos pares da tupla original, na mesma ordem em 
    que se encontravam.
    int->int"""
    if t[0]%2 == 0:
        a = (t[0],)
        return a