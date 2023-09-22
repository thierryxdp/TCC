def media_matriz(matriz):
    soma = 0
    tamanho = 0

    for linha in matriz:
        soma += round(linha,2)
        tamanho += len(linha)

    return soma / tamanho