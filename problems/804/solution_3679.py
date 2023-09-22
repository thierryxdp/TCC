def filtra_pares(tupla):
    '''função que recebe uma tupla com 4 números inteiros e retorna uma tupla que
       contém só os elementos pares desta tupla. tuple(int,int,int,int) -> tuple'''
    t1 = tupla
    if (t1[0] % 2 == 0):
        t2 = () + t1[0]
        if (t1[1] % 2 == 0):
        t2 = () + t1[1]
        if (t1[2] % 2 == 0):
        t2 = () + t1[2]
        if (t1[3] % 2 == 0):
        t2 = () + t1[3]
        return t2