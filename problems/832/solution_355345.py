def eh_quadrada(matriz):
    '''função que verifica se uma matriz é quadrada, ou seja, se possui o mesmo número de linhas e colunas, a partir de uma matriz de entrada; list(lists) -> bool'''
    
    if len(matriz) == len(matriz[0]) or matriz[0]==[]:
        return True
    
    else: 
        return False