def media_matriz(matriz):
    soma = 0
    for linha in matriz:
        for aij in linha:
            soma = soma + aij
    total = len(matriz)*len(matriz[0])
    return round(soma/total,2)