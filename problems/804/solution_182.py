def filtra_pares(tup):
    """Recebe uma tupla com 4 inteiros e retorna uma nova tupla apenas com os números pares; tuple -> tuple"""
    if tup[0]%2==0 and tup[1]%2==0 and tup[2]%2==0 and tup[3]%2==0:
        return tup
    elif tup[0]%2==0 and tup[1]%2==0 and tup[2]%2==0 and tup[3]%2!=0:
        return tup[0], tup[1], tup[2]
    elif tup[0]%2==0 and tup[1]%2==0 and tup[2]%2!=0 and tup[3]%2!=0:
        return tup[0], tup[1]