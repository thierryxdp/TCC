def media_matriz(m):
    """ retorna a media de todos os numeros de uma matriz;
    list -> float"""
    soma = 0
    for x in range(len(m)):
        soma = soma + sum(m[x])
    media = round((soma/len(m[1])),2)
    return media