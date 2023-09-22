def eh_quadrada(matriz):
    '''Função que verifica se uma matriz é quadrada
    valor de entrada:lista
    valor de saída: bool'''
    
    if len(matriz) == 0:
        return True
    
    matriz2= matriz[:]
    separada= matriz2.pop(0)
    
    if len(separada) == len(matriz):
        return True
    else: 
        return False