def qtd_divisores(n):
    '''Conta quantos divisortes tem um numero(n)'''
    divisores = 0
    for i in range(n+1):
        if i < 0:
            if n % 1 == 0:
                divisores = divisores + 1
        elif n % i == 0:
            divisores = divisores + 1
    return divisores