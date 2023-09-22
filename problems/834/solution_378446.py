def media_matriz(matriz):
    c = 0
    l=0
    for lin in matriz:
        for col in lin:
            c = c + col 
        l = l + len(lin)
    return round (c/l,2)