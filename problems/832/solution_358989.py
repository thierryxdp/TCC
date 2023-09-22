def eh_quadrada(matriz: list)-> bool:
    """Dada uma matriz, identifica se a matriz é quadrada."""
	n_linhas = len(matriz)
	n_colunas = len(matriz[0])

    if ((n_linhas == n_colunas) or (matriz == [])):

        return True
    else:
        return False