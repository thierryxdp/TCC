def soma_h(N):
    '''
       Função que calcula e retorna o valor de h, com h sendo a soma de 1 até 1/N com 2 casas decimais.
       int -> float
    '''
    H = 0
    for elem in range(1,N+1):
        H = H + 1/elem
    return round(H,2)