def eh_quadrada(matriz):
    '''Funcao que indentifica se uma matriz e quadrada.
    lista->bool'''
    x=0
    k=len(matriz)
    if len(matriz)!=len(matriz[0]):
        return False
                        
    while x in k:
        if matriz[x]==k:
        x=x+1
        return True