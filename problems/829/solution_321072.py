def soma_h (N):
    '''Função que retorna o valor de H dado um número N de entrada. H=1+1/2+1/3+...+1/N.
    int -> float'''
    H = 0
    for i in range(1,N+1):
        H = H + (1/i)
    return round(H,2)