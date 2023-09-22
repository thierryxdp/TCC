def eh_quadrada(matriz):
    """
    	Função que identifica se uma matriz é quadrada ou 
        não.
        list(list) -> bool
    """
    nlinhas = len(matriz)
    ncolunas = len(matriz[0])
    if nlinhas == ncolunas:
        return True

    else:
        return False