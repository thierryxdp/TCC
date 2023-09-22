def media_matriz(matriz):
    soma = 0
    tamanho = 0
    
    for linha in matriz:
        soma += sum.round(linha)
        tamanho += len(linha)

    return soma / tamanho