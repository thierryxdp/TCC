def eh_quadrada(matriz):
    quadrada=False
    tamanho_linha=len(matriz)
    if tamanho_linha<= 0:
        quadrada=True
    else:
        tamanho_coluna=len(matriz[0])
        if tamanho_coluna==tamanho_linha:
            quadrada=True
    return quadrada