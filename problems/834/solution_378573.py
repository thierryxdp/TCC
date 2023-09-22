def media_matriz(matriz):
    quant=0
    total=0
    for i in matriz:
        total += sum(i)
        quant += len(i)
    return total/quant