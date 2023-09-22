def fatorial(n):
    '''função que dado um número calcula o fatorial deste número'''
    fatoracao = n
    while n > 1:
        fatoracao *= n - 1
        n -= 1

    return fatoracao