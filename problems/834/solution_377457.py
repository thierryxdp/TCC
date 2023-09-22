def media_matriz(matriz):
    """	função que recebe uma matriz e retorna a média dos elementos que a compõe
    	entrada: lista
        saida: float
    """
    lista1 = []
    
    for lista in matriz:
        lista1 += lista[::]
    media = round(sum(lista1)/len(lista1),2)
    return media