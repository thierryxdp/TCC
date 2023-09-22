def eh_quadrada(matriz):
    '''Funcao que recebe uma matriz nao-vazia e retorna se a mesma e ou nao
    uma matriz quadrada.
    list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False1