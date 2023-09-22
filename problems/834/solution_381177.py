def media_matriz(matriz):
    total = count = 0
    for linha in matriz:
        for valor in linha:
            count += 1
            total += valor
    return total / count