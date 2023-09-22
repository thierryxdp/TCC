def eh_quadrada(matriz):
    """Funcao que dada uma matriz identificar se ela e quadrada
    list --> bool"""
    n_linha = len(matriz)
    if n_linha == 0:
        quadrada = True
    elif n_linha != 0:
        n_coluna = len(matriz[0])
        if n_linha == n_coluna:
            quadrada = True
    else:
        quadrada = False
    return quadrada