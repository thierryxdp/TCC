def eh_quadrada(matriz):
    for c in range(len(matriz)):
        if (len(matriz)==len(matriz[c]))==False:
            return False
    return True