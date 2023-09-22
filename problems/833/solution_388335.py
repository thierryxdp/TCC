def conta_numero(n,mat):
    qtd=0
    for linhas in mat:
        for elementos in linhas:
            if elementos == n :
                qtd+=1
    return qtd