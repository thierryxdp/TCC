def media_matriz(matriz):
    i = 0
    j = 0

    for x in matriz:
        for y in x:
            i += y
            j += 1
            
    m = i/j

    return round(m, 2)