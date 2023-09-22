def media_matriz(matriz):
    soma = 0
    quantidade = 0
    for x, y in enumerate(matriz):
        for z in matriz(x):
            soma = soma + z
            quantidade = quantidade + 1
    media = soma / quantidade
    return media