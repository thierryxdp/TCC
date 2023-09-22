def eh_quadrada(matriz):
    '''
    Recebe uma matriz (lista de listas de números) e retorna se ela é quadrada ou não (mesmo número de linhas e colunas).
    list(list)-> bool
    '''
    for i in range(len(matriz)):
        j = len(i)
        if len(j) == len(i):
            return True
        else:
            return False