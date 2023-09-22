def filtra_pares(tup):
    """Recebe uma tupla com quatro elementos e retorna uma nova tupla apenas com os elementos pares; tupla -> tupla"""
    if tup[0]%2==0:
        return tup[0]
    elif tup[1]%2==0:
        return tup[1]
    elif tup[2]%2==0:
        return tup[2]
    elif tup[3]%2==0:
        return tup[3]
    else:
        return