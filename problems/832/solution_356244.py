def eh_quadrada(numero_linhas, numero_colunas):
    """função para identificar se uma matriz é quadrada ou não"""
    matriz = []
    for _ in range(n_linhas):
        matriz.append( [" "] * n_colunas )
        if numero_linhas == numero_colunas:
            return True
        else:
            return False