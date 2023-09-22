def soma_h(N):
    '''Funcao que calcula uma soma de fracao onde o ultimo termo da
soma tem como divisor o numero n dado
int->float'''
    soma=0
    for x in range(1,N+1):
        inverso=(1/x)
        soma= soma + inverso
    return round(soma,2)