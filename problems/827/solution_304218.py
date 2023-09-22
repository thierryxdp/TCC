qtd_divisores(n):
    '''Função que dado um numero de entrada, caonta quantos numeros ele tem como divisor.
    int -> int'''
    d = 0
    for i in range(1,n+1):
        if n % i == 0:
            d += 1
    return d