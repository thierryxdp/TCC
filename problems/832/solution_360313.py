def eh_quadrada(A):
    ''' recebe uma matriz e verifica se ela é quadrada (mesmo número de linhas e colunas)
    list(list)->boolean'''
    if len(A) == len(A[0]):
        return True
    if len(A) == 0:
        return True
    else:
        return False