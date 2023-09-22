def eh_quadrada(A):
    '''Funcao que diz se a matriz e quadrada ou nao'''
    '''list -> bool'''
    tamanho = 0
    for linha in A:
        tamanho += len(linha)
        for tamanho == len(linha):
            return True
    return False