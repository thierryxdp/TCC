def eh_quadrada(matriz):
    '''Funcao que identifica se uma matriz e quadrada
    list(list) -> bool'''
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna or matriz==[[]]:
        return True
    else:
        return False