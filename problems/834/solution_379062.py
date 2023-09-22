def media_matriz(matriz):
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    i = 0
    j = 0
    soma = 0
    list = []
    a = 0
    while i < nlinha:
        while j < ncoluna:
            coluna = matriz[a]
            soma = soma + coluna[j]
            j = j + 1
            a = a + 1
        list.append(soma)
        i = i + 1
    valor = soma/nlinha*ncoluna
    return list