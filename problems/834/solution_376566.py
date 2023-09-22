def media_matriz(matriz):
    return round(sum(sum(linha) for linha in matriz) / len(matriz) * len(matriz[0]), 2)