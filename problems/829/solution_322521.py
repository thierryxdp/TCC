def soma_h(N):
    '''Retorna o valor de H com N termos, onde N é inteiro e dado
    como entrada
    '''
    H = 0
    for x in range(1,N+1):
        H = H + 1/x
    return round(H,2)