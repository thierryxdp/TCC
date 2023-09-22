def media_matriz(m):
    soma = 0
    for linha in m:
        for aij in linha:
            soma += aij
    return soma/len(m)