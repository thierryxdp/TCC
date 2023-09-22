def conta_numero(n,M):
    linha=0
    contador=0
    for x in M:
        contador=contador+list.count(M[linha],n)
    linha=linha+1
    return contador