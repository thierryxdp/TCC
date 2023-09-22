def media_matriz(matriz):
    soma = 0
    tamanho = 0

    for linha in matriz:
        soma += sum(linha,0)
        tamanho += len(linha)

    return soma / tamanho