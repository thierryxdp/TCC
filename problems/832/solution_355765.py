def eh_quadrada(matriz):
    """
    Função para determinar se uma matriz é quadrada ou não.
    matriz - é a matriz que se deseja saber se é quadrada.
    list(list) -- > bool
    """
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    if n_linha == n_coluna or n_linha == 1:
        return True
    else:
        return False