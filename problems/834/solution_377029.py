def media_matriz(matriz):
    '''list(list) -> float'''
    qtd = 0
    soma = 0
    for j in matriz:
        for i in j:
            soma += i
            qtd += 1
    media = round((soma/qtd), 2)

    return media