def eh_quadrada(matriz):
    '''A partir de uma matriz retorna se ela é ou nao uma matriz quadrada
       parameters:
       matriz: matriz de analise
       list->bool'''
    none=[]
    if matriz==none:
        return True
    while len(matriz) > 0 and len(matriz[0]) > 0:
        if len(matriz)!=len(matriz[0]):
            return False
        else:                   
            return True