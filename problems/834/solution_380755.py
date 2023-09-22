def media_matriz(matriz):
    total = 0
    soma = 0
    for linha in matriz:
        for itens in linha:
            soma = soma + itens
            total = total + 1
    return soma/total