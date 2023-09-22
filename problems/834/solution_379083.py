def media_matriz(matriz):
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    i = 0
    soma = 0
    while i < nlinha:
        j = 0
        while j < ncoluna:
            coluna = matriz[i]
            soma = soma + coluna[j]
            j = j + 1
        i = i + 1
    valor = soma/nlinha*ncoluna
    return nlinha*ncoluna