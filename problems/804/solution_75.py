def filtra_pares (elementos):
    """retorna os números pares de um conjunto de 4 elementos"""
    tupla=()
    if elementos[0]%2=0:
        tupla=tupla+elementos[0]
    elif elementos[1]%2=0:
        tupla=tupla+elementos[1]
    elif elementos[2]%2=0:
        tupla=tupla+elementos[2]
    elif elementos[3]%2=0:
        tupla=tupla+elementos[3]
    return tupla