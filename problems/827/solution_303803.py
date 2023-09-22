def qtd_divisores(n):
    '''Dado um número inteiro, retorna a quantia de 
    divisores desse número.
    int --> int'''
    proximo = 1
    counter = 0
    while proximo != n:
        if n<0:
            return 0
        if n%proximo == 0:
            counter = counter + 1
        proximo = proximo + 1
    return counter + 1