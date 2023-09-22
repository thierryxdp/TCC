def media_matriz(m):
    soma = 0
    for j in m:
        soma += sum(j)
    return round(soma/(len(m)*len(m[0])), 2)