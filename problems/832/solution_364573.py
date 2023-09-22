def eh_quadrada(matriz):
    """Dado uma matriz qualquer como entrada, determinar se é quadrada ou não; list -> str"""
    linha = len(matriz)
    coluna = len(matriz[0])
    if linha == coluna:
        for i in range(linha):
            for j in range(coluna):
                if matriz[i>0][j>0] != []:
                    return True
    else:
        return False