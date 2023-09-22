def media_matriz(matriz):
    nlinha = len(matriz)
    ncoluna = len(matriz[0])
    i = 0
    j = 0
    soma = 0
    while i < nlinha:
        while j < ncoluna:
            coluna = matriz[i]
            lista = coluna
            soma = soma + lista[j]
            j = j + 1
        i = i + 1
    valor = soma/nlinha*ncoluna
    return soma