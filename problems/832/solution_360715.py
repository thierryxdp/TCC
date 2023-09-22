def eh_quadrada(matriz):
    '''Função que verifica se uma matriz é quadrada
    valor de entrada:lista
    valor de saída: bool'''
    matriz2= str(matriz)
    separada= matriz2.split(' ')
    if matriz==[]:
        return True
    if len(matriz)== len(separada[0]):
        return True
    else:
        return False