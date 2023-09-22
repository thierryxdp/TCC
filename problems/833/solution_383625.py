def conta_numero(numero, matriz):
    i = len(matriz)
    j = len(matriz[0])
    count = 0
    if(j == 0):
        return count
    else:
        for x in range(0, i):
            for k in range(0, j):
                if(numero == matriz[x][k]):
                    count = count + 1
    return count