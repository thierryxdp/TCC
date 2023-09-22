def conta_numero(n,M):
    linha=0
    conta=[]
    for x in M:
        quant=list.count(M[linha],n)
        list.append(conta,quant)
    linha=linha+1
    return sum(conta)