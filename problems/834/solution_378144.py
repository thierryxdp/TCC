def media_matriz(m):
    soma = 0 
    divisor = len(m) * len(m[0])
    for lista in range(len(m)):
        soma += sum(m[lista])
    return soma / divisor