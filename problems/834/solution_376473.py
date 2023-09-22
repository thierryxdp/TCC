def media_matriz(matriz):
    """calculo e retorno de uma funçao que da a media de uma matriz."""
    soma = 0
    o = 0
    for linha in matriz:
        soma += sum(linha)
        o += len(linha)
    p=soma/o

    return round(p,2)