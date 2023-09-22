def media_matriz(matriz):
    """	função que recebe uma matriz e retorna a média dos elementos que a compõe
    	entrada: lista
        saida: float
    """
    media = round(sum(matriz)/len(matriz),2)
    return media