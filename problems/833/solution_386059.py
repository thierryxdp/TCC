def conta_numero(n,M):
    linha=0
    vezes=0
    for i in M[linha]:
            if i==n:
                vezes+=1  
        linha=linha+1
    return vezes