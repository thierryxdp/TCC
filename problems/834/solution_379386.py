def media_matriz(matriz):
    """retorna a media de todos os numeros da matriz; list -> float"""
    n=len(matriz)*len(matriz[0])
    a=0
    for x in matriz:
        for y in x:
            a=a+y
    return round(a/n,2)