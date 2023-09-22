def media_matriz(matriz):
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
        somaf =soma/tamanho
        somaf = round(somaf,2)
    return somaf