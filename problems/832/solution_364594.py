def eh_quadrada(matriz):
    '''verifica se tal matriz é quadrada.
    matriz->bool'''
    a=True
    if len(matriz[0])!=len(matriz):
   		a=False
    return a