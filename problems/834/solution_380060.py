def media_matriz(m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    soma=0
    media=0
    a=0
    for i in qtd_linhas:
        for j in qtd_colunas:
            soma = list(map(sum, m))
            a=sum(soma)
    return a/(qtd_linhas*qtd_colunas)-1