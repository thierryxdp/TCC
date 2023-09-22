def eh_quadrada(matriz):
    '''Função que verifica se uma matriz é quadrada
    valor de entrada:lista
    valor de saída: bool'''
    separada=matriz.pop(0)
    if len(separada) == len(matriz)+1:
        return True
    if len(matriz) == 0:
        return True
    else: 
        return False