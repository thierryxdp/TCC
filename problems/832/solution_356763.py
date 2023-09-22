def eh_quadrada(matriz):
    '''Identifique se uma matriz é quadrada ou não; sem entrada -> lista'''
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
                       if len(matriz)==len(matriz[i]):
                       	return True
    else:
        return False