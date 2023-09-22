def qtd_divisores(N):

    final= 0
    
    for d in range((1),N+1):
        if N%d== 0:
            final+= 1
            
    return final