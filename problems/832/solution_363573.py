def eh_quadrada(matriz):
    l = 0
    c = 0
    for x in matriz:
        for y in matriz:
            l = l+1
            c = c+1
    if l == c:
        return True
    else:
        return False