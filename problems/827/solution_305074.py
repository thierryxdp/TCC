def qnt_divisores(n):
    '''Dado um numero n, retorna a quantidade de divisores que esse numero tem.
    int -> int'''
    for i in range(1, int(n / 2) + 1):
        if n % i == 0:
            yield i