def eh_quadrada(matriz):
    '''Identifique se uma matriz é quadrada ou não; sem list -> bool'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i==0 and j==0:
                return True
            if len(matriz)==len(matriz[i]):
                return True
    else:
        return False