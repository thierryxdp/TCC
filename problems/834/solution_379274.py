def media_matriz(m):
    soma = 0
    nlin = len(m)
    ncol = len(m[0])
    for linha in m:
        for valor in linha:
            soma = soma + valor
    	media = soma/(nlin*ncol)
    return round(media, 2)