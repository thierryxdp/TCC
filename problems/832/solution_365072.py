def eh_quadrada(matriz):
    resultado = False
    tamanho_linha = len(matriz)
    if tamanho_linha <= 0:
        resultado=True
    else:
        tamanho_coluna=len(matriz[0])
        if tamanho_coluna == tamanho_linha:
            resultado = True
    return resultado