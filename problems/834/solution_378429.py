def media_matriz(matriz):
    i = 0
    total = 0
    while i < len(matriz):
        total = total + sum(matriz[i])
        i = i + 1
    return total/(i-1)