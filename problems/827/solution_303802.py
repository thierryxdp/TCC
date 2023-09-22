def qtd_divisores(n):
    '''Dado um número inteiro, retorna a quantia de 
    divisores desse número.
    int --> int'''
    proximo = 1
    counter = 0
    while proximo != abs(n):
        if abs(n)%proximo == 0:
            counter = counter + 1
        proximo = proximo + 1
    return counter + 1