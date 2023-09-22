def eh_quadrada(A):
    """ Essa função recebe uma matriz e verifica se é 
    quadrada. matriz->bool."""
    if A == []:
        return True
    num_linhas_A,num_colunas_A = len(A), len(A[0])
    if num_linhas_A == num_colunas_A:
        return True
    elif num_linhas_A != num_colunas_A:
        return False
    else:
        return True