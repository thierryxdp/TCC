def soma_h(N):
    '''Dado um numero(N),calcula uma função fracional de numerador 1 onde o denominador é uma crescente que vai ate N.int->float'''
    i=0.0
    for N in range(1,N+1):
        i=i+(1.0/N)
    return round(i,2)