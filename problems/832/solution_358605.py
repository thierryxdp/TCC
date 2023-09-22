def eh_quadrada(matriz):
    """
    Essa função verifica se uma matriz é quadrada comparando as linhas e colunas
    Parametros: matriz (lista)
    Saida: bolean
    """
    if matriz == []:
        return True
    else:
        return len(matriz)==len(matriz[0])