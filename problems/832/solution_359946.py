def eh_quadrada(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if range(j) == range(i):
                return False
            else:
                return True