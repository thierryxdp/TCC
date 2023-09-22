def media_matriz(matriz):
    """a função retorna a media entre matrizes usando o laço for"""
    soma = 0
    tamanho = 0
    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)
    return round(soma / tamanho,2)