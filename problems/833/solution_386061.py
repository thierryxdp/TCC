def conta_numero(n,M):
    '''conta quantas vezes um numero aparece em uma matriz;
    int->list'''
    linha=0
    vezes=0
    for x in M:
        for i in M[linha]:
            if i==n:
                vezes+=1  
        linha=linha+1
    return vezes