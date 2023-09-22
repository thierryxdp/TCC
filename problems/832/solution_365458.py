def eh_quadrada(matriz):

    tam = len(matriz)
    if tam == 0:
        return True
    
    tam2 = len(matriz[0])

    if tam2 == tam:
        return True
    else:
        return False