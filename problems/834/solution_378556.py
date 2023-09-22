def media_matriz(matriz):
    soma=0
    for coluna in matriz:
        for linha in matriz:
            if coluna != 0:
                soma = soma + 1
    div = len(matriz)* len(matriz[0])
    return round(soma/div,2)