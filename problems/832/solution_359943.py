def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if j == i:
                return True
            else:
                return False