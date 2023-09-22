def eh_quadrada(matriz):
    '''define se uma matriz é quadrada, retorna True caso seja e False caso
    o contrário; list -> bool'''
    #seja uma matriz uma lista de listas com elementos matriz[i][j]
    if len(matriz) == 0:
        return True
    return len(matriz) == len(matriz[0]):