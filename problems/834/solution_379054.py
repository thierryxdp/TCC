def media_matriz(matriz):
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    i = 0
    j = 0
    soma = 0
    list = []
    while i < nlinha:
        while j < ncoluna:
            coluna = matriz[i]
            soma = soma + coluna[j]
            list.append(soma)
            j = j + 1
        i = i + 1
    valor = soma/nlinha*ncoluna
    return