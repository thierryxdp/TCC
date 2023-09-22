def eh_quadrada(matriz):
    '''verifica se tal matriz é quadrada.
    matriz->bool'''
    a=True
    for i in range(len(matriz)):
        if len(matriz[i])!=len(matriz):
            a=False
    return a