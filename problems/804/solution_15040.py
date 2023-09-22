def filtra_pares(n):
    """Função que filtra os numero pares de uma tupla
    tuple -> int"""
    tupla = ()
    if n [0]%2 == 0:
        tupla = tupla + (n[0],)
    if n [1]%2 == 0:
        tupla = tupla + (n[1],)
    if n [2]%2 == 0:
        tupla = tupla + (n[2],)
    if n [3]%2 == 0:
        tupla = tupla + (n[3],)
    return tupla