def qtd_divisores(n):
    '''Dado um número n retorna os seus divisores
    int -> list'''
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1
    return divisores