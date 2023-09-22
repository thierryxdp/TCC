def filtra_pares(tup):
    """Essa função recebe uma tupla com 4 elementos inteiros e retorna
    só os pares na ordem crescente que estavam. tup - > tup"""
    x1 = tup[0]//2
    x2 = tup[1]//2
    x3 = tup[2]//2
    x4 = tup[3]//2 
    if x1%2 == 0 and x2%2 == 0 and x3%2 == 0 and x4%2 == 0:
        return tup[0:]