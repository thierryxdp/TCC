def media_matriz(matriz):
    soma = 0
    tamanho = 2
    
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)

    return soma / tamanho