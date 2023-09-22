def conta_numero(num,matriz):
    total=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == num:
                total = total +1
    return total