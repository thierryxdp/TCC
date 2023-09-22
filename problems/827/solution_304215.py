qtd_divisores(n):
    '''Função que dado um numero de entrada, caonta quantos numeros ele tem como divisor.
    int -> int'''
    d=1
    for i in range (1,x+1):
        if x % i == 0:
            d += 1
    return d