def qtd_divisores(n):
    '''conta quantos divisores um número tem'''
    divisores = 0
    for i in range (1, n):
        if n%i == 0:
            divisores = divisores + 1
            return divisores