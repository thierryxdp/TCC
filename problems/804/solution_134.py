def filtra_pares(tup):
    """Recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os pares; tup -> tup"""
    if tup[0]%2==0:
        return tup[0]
    elif tup[1]%2==0:
        return tup[1]
    elif tup[2]%2==0:
        return tup[2]
    elif tup[3]%2==0:
        return tup[3]