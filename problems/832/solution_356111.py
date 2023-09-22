def eh_quadrada(matriz):
    for c in matriz:
        if (len(matriz)==len(matriz[c]))==False:
            return False
    return True