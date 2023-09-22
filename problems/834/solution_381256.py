def media_matriz(matriz):
    resultado=0
    for linha in matriz:
        resultado+= linha.count(matriz)
        for coluna in matriz:
            resultado+=coluna.count(matriz)
    return resultado