def eh_quadrada(matriz):
    '''determina se uma matriz é quadrada. Caso seja, retorna True, do
    contrário, False; list -> bool'''
    #seja uma matriz uma lista de listas com elementos como matriz[i][j]
    i = matriz.index
    j = matriz[1].index
    while i and j in matriz:
        if i == j:
            return True
        if i != j:
            return False