def fatorial(num):
    '''crie uma função que, dado um número, retorne o cálculo do fatorial desse número. int-->int.'''
    fatorial = 1
    if num<2:
        return 1
    while num >= 1:
        fatorial = fatorial*num
        num = num-1
    return fatorial