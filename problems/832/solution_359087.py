def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada.
    lista->bool'''
    if len(matriz)==0:
        return True
    if len(matriz)!=len(matriz[0]):
        return False
    x=0
    k=len(matriz)
    z=range(k)
    while x in z:
        if len(matriz[x])==k:
   			x=x+1
    return True