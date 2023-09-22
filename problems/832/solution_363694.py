def eh_quadrada(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if len(matriz) == len(matriz[i]) and len(matriz[j]):
                return True

            else:
                return False

    return True