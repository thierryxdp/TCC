def qtd_divisores(n):
    '''Dado um numero n, retorna quantos divisores esse numero possui.
    int -> int'''
    div = 0

    for i in range(1, n+1):
        if n % i == 0:
            div += 1
    return div