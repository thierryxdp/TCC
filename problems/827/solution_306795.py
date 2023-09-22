def qtd_divisores(n):
    '''Conta quantos divisortes tem um numero(n)'''
    divisores = 0
    for x in range(n):
        if x <= 0:
            if n % 1 == 0:
                divisores = divisores + 1
        elif n % x == 0:
            divisores = divisores + 1
    return divisores