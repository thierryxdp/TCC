def media_matriz(m):
    soma = 0
    for i in m:
        for c in i:
            soma = (soma + c)/len(m)*len(m[0])
    return soma