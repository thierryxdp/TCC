def eh_quadrada(A,B):
    ''' recebe duas matrizes e verifica se elas são quadradas (mesmo número de linhas e colunas)
    list(list),list(list)->boolean'''
    if len(A)== len(B[0]) and len(B)==len(A[0]):
        return True
    else:
        return False