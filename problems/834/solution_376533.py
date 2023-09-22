def media_matriz(m):
    """ retorna a media de todos os numeros de uma matriz;
    list -> float"""
    soma = 0
    div = 0
    for x in range(len(m)):
        for y in range(len(m[x])):
            soma = soma + m[x][y]
            div = div + 1
    media = round(soma/div,2)
    return media