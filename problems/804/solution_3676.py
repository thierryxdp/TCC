def filtra_pares(tupla):
    '''função que recebe uma tupla com 4 números inteiros e retorna uma tupla que
       contém só os elementos pares desta tupla. tuple(int,int,int,int) -> tuple'''
    if (tupla[0] % 2 == 0):
        return tupla[0]
    if (tupla[1] % 2 == 0):
        return tupla[1]
    if (tupla[2] % 2 == 0):
        return tupla[2]
    if (tupla[3] % 2 == 0):
        return tupla[3]