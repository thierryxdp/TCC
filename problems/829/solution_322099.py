def soma_h(N):
    '''Calcula e retorna o valor H de modo que 
    H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/N
    Int -> Float'''
    H =1
    for i in range (2,N+1):
        H += 1/i
    return round(H,2)