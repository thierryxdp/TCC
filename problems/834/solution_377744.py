def media_matriz(matriz):
    """Dado uma matriz, retorna a média da soma de todos números da matriz. list>float"""
    y=0
    x=0
    for a in matriz:
        for b in a:
            y+=b
            x+=1
    return round(y/x,2)