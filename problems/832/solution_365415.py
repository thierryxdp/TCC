def eh_quadrada(matriz):

    tam2 = len(matriz)
    if tam2 == 0:
        return True
    
    tam1 = len(matriz[0])

    if tam1 == tam2:
        return True
    else:
        return False