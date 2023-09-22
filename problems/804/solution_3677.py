def filtra_pares((tupla)):
    '''função que recebe uma tupla com 4 números inteiros e retorna uma tupla que
       contém só os elementos pares desta tupla. tuple(int,int,int,int) -> tuple'''
    t = tupla
    if (t[0] % 2 == 0):
        return t[0]
    if (t[1] % 2 == 0):
        return t[1]
    if (t[2] % 2 == 0):
        return t[2]
    if (t[3] % 2 == 0):
        return t[3]