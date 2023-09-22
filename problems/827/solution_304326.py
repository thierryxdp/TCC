def qtd_divisores(n):
    '''Função que dado um número "n" como entrada, retorna a quantidade de
    divisores que esse mesmo número tem.'''
    divisores = 0
    for i in range(1, n+1):
        if (n % i) == 0 :
            divisores += 1
    return divisores