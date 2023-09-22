def eh_quadrada(matriz):

    '''
    Função que recebe uma matriz como parâmetro e retorna
    True caso ela seja Quadrada(mesmo número de linhas e
    colunas) ou False, caso contrário.
    '''

    lin = len(matriz)
    col = len(matriz[0])
    
    if lin == col:
        return True
    else:
        return False