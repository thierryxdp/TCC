def qtd_divisores(n):
    '''função que conta o numero de divisores de um numero dado
    int->int'''
    divisores=1
    if n < 0:
        return 0
    for i in range(1, int(n//2+1)):
        if n % i == 0:
            divisores=divisores+1

    return divisores