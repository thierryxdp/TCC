def eh_quadrada(matriz):
    '''Retorna se a dada matriz é quadrada
    list -> bool'''
    return (len(matriz) == 0) or bool(min([1] + [0 for i in range(len(matriz)) if len(matriz[i]) != len(matriz) ]))