def media(matriz):
    """função que calcula e retorna a media de uma matriz
    lista(matriz) -> float"""
    soma = 0
    tamanho = 0

    for linha in matriz:
        soma += sum(linha)
        tamanho += len(linha)

    return round((soma / tamanho),2)