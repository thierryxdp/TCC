def conta_numero(n,M):
    linha=0
    colunas=0
    for x in M:
        quant=list.count(M[linha],n)
        linha+=1
    return quant