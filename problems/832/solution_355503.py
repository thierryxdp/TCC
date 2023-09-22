def eh_quadrada(matriz):
    '''Funcao que recebe uma matriz e indentifica se é o não quadrada
    list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    for i in matriz:
        if linha == coluna:
            return True
        else:
            return False