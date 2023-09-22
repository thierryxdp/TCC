def eh_quadrada(A):
    '''Funcao que diz se a matriz e quadrada ou nao'''
    '''list -> bool'''
    for linha in A:
        tamanho += len(linha)
        if tamanho == len(linha):
            return True
        else:
            return False