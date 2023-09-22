def media_matriz(m):
    qtd_linhas=len(m)
    qtd_colunas=len(m[0])
    soma=0
    media=0
    a=0
    for i in range(qtd_linhas):
        for j in range(qtd_colunas):
            soma = list(map(sum, m))
            media=sum(soma)
            a/(qtd_linhas*qtd_colunas)       
            media=a/(qtd_linhas*qtd_colunas) 
    return media