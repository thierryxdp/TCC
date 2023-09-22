def media_matriz(M):
    nlinhas = len(M)
    ncolunas = len(M[0])
    soma = 0 
    qtd_elem = 0
    for i in range(nlinhas):
        for j in range(ncolunas):
            soma = soma + M[i][j]
            qtd_elem = qtd_elem + 1
    media = soma/qtd_elem
    return round(media,2)