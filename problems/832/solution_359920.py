def eh_quadrada(matriz):
    '''
    Recebe uma matriz (lista de listas de números) e retorna se ela é quadrada ou não (mesmo número de linhas e colunas).
    list(list)-> bool
    '''
    for i in range(len(matriz)):
        for j in range(len(i)):
            if i != j:
                return False
            else:
                return True