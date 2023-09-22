def fatorial(n):
    '''Função que dado um número, calcule o fatorial desse número.
       int ---> int'''
    produto = 1
    for fator in range(n,1,-1):
        produto = produto * fator
    return produto