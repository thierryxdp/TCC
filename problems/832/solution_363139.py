def eh_quadrada(matriz):
    """Funcao que dada uma matriz identificar se ela e quadrada
    list --> bool"""
    n_linha = len(matriz)
    n_coluna = len(matriz[0])
    if n_linha == n_coluna:
        quadrada = True
    else:
        quadrada = False
    return quadrada