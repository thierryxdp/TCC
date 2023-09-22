def eh_quadrada(matriz):
    '''funcao que retorna True caso a matriz dada como parametro de entrada
       seja uma matriz quadrada, se nao for retorna False
       list->bool'''
    if matriz==[]:
        return True
    
    elif len(matriz)==len(matriz[0]):
        return True
    else:
        return False