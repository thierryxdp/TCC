def eh_quadrada(matriz):
    '''analisa se uma matriz e quadrado ou nao
       list -> bool'''
    
    if matriz==[]:
        return True
    
    if len(matriz)==len(matriz[0]):
        return True
    else:
        return False