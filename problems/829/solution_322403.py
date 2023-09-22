def soma_h(N):
    '''Coloque um numero(N) e o resultado será 1 + 1/2 + 1/3 + ... + 1/N
       int->float'''
    numero=0
    for i in range(1, N+1):
        numero=numero+1/i
    return round(numero,2)