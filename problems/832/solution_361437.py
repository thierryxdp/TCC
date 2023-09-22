def eh_quadrada(matriz):
    '''Função que ao receber uma matriz verifica se ela é quadrada.'''
    #list -> bool
    if matriz == []:
        return True
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if len(matriz) == len(matriz[i]) and len(matriz[j]):
                return True
            else:
                return False