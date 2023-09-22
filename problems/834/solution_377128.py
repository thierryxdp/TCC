def media_matriz(m):
    denominador = len(m)*len(m[0])
    soma = 0
    for i in m:
        for c in i:
            soma = c /denominador
    return soma