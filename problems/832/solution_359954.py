def eh_quadrada(matriz):
    if len(matriz) == 0:
        return True
    for i in range((matriz[0])):
        for j in range(len(matriz[0])):
            if len(matriz[i]) == len(matriz[j]):
                return False
            else:
                return True