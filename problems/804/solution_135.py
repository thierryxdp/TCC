def filtra_pares(tup):
    """Recebe uma tupla com quatro elementos inteiros como parâmetro e retorna uma nova tupla contendo apenas os pares; tup -> tup"""
    if tup[0]%2==0:
        n1 = tup[0]
        return n1
    elif tup[1]%2==0:
        n2 = tup[1]
        return n2
    elif tup[2]%2==0:
        n3 = tup[2]
        return tup[2]
    elif tup[3]%2==0:
        n4 = tup[3]
        return tup[3]