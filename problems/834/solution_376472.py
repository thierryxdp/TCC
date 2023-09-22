def media_matriz(matriz):
    soma = 0
    o = 0
    for linha in matriz:
        soma += sum(linha)
        o += len(linha)
    p=soma/o

    return round(p,2)