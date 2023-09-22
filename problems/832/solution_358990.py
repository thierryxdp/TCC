def eh_quadrada(matriz: list)-> bool:
    """Dada uma matriz, identifica se a matriz é quadrada."""
    n_linhas = len(matriz)

    if (len(matriz) == 0):
        return True
    else:
        n_colunas = len(matriz[0])
        if ((n_linhas == n_colunas)):
            return True
        else:
            return False