def media_matriz(matriz):
    """função que retorna a média de todos os numeros de uma matriz
    list -> float"""
    c = 0
    l=0
    for lin in matriz:
        for col in lin:
            c = c + col 
        l = l + len(lin)
    return round (c/l,2)