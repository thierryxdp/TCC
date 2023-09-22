def eh_quadrada(A):
    """ Essa função recebe uma matriz e verifica se é 
    quadrada. matriz->bool."""
    num_linhas_A,num_colunas_A = len(A), len(A[0])
    matriz = []
    if A == matriz:
        return True
    elif num_linhas_A == num_colunas_A:
        return True
    elif num_linhas_A != num_colunas_A:
        return False