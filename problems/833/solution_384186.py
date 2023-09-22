def conta_numero(n,M):
    """Funcao que dado um numero inteiro n e uma matriz M de
    inteiros de tamanho qualquer, conta e retorna quantas 
    vezes aquele numero aparece na matriz;
    int,lista->int"""
    
    Q=0
    
    for i in range(len(M)):
        for j in range(len(M[i])):
            if M[i][j]==n:
                Q=Q+1
                
    return Q