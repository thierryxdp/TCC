def media_matriz(matriz):
    """calculo e retorno da matriz de uma funçao"""
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    p=soma/tamanho

    return round(p,2)