def media_matriz(matriz):
    """Calcula a media de uma matriz pela divisao da soma dos elementos pel quantidade de elementos; list=>float"""
    soma = 0
    tamanho = 0

    for linha in matriz:
        soma =soma+ sum(linha)
        tamanho =tamanho+ len(linha)

    return round((soma/tamanho),2)