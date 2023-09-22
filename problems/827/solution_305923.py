def qtd_divisores(n):
    '''Função que dado um número de entrada retorne a 
    quantidade de divisores que tal número tem.
    int --> int.'''
    for x in range(n, n//2+1):
        if n % x == 0:
            return x
    return n