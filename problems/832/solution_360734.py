def eh_quadrada(matriz):
    '''Função que verifica se uma matriz é quadrada
    valor de entrada:lista
    valor de saída: bool'''
    if len(matriz) == 0:
        return True
    if len(matriz.pop(0)) == len(matriz):
        return True
    else: 
        return False