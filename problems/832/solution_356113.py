def eh_quadrada(matriz):
    c=0
    while c in len(matriz):
        if (len(matriz)==len(matriz[c]))==False:
            return False
    c=c+1
    return True