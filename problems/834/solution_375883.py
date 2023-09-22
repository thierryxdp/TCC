def media_matriz(m):
    soma = 0
    tamanho = 0
    for linha in matriz:
    soma += sum(linha)
    tamanho += len(linha)
    return soma / tamanho