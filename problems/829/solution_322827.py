def soma_h(N):
    '''
        Funcao recebe um numero inteiro N e
        retorna a soma H com N termos.
        int -> float
        
    '''
    # H = 1 + 1/2 + 1/3 + 1/4 +...+ 1/N
    H = 1
    for num in range(2,N+1):
        H = round((H + round(1/num,2)),2)
    return H