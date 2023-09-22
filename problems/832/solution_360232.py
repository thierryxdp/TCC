def eh_quadrada(matriz):
    nlin = len(matriz)
  

    for i in range(len(matriz)):
        if not len(matriz[i]) == nlin:
            return False

    for j in range(len(matriz[0])):
        if not len(matriz[j]) == len(matriz[0]):
            return False

    return True