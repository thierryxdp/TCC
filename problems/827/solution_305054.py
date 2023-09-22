def qtd_divisores(n):
    '''Conta quantos divisores o número de entrada possui
    int -> int'''
    divisores = 0
    for i in range(1,n+1):
        if n % i == 0:
            divisores += 1
    return divisores