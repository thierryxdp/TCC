def soma_h(N):
    '''função que, dado um número N inteiro, 
    retorna o valor de H com N termos.
    int -> float'''
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
    return round(H,2)