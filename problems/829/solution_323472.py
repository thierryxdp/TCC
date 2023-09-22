def soma_h (N):
    '''retorna o valor H dado um valor N
    int->float'''
    soma = 0
    for i in range(1,N+1):
        soma += 1/i
    return round(soma,2)