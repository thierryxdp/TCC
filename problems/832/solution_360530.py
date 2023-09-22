def eh_quadrada(matriz):
    '''funcao que retornar em dado 
    booleano se uma matriz é quadrada
    entrada: lista
    saida: booleano
    '''
    if len(matriz)==0:
        return True 
    if len(matriz)==len(matriz[0]):
        return True 
    else:
        return False