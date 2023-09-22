def fatorial(n):
    '''fatorial recebe um numero inteiro n e devolve o fatorial deste número.
    int-->int'''
    i=1
    multiplicacao=n
    while i<n:
        multiplicacao=multiplicacao*i
        i=i+1
    return multiplicacao