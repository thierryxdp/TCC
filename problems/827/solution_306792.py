def qtd_divisores(n):
    '''Conta quantos divisortes tem um numero(n)'''
    divisores = 0
    for i in range(n+1):
        if n % i == 0:
            divisores = divisores + 1
    return divisores