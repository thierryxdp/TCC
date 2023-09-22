def fatorial(n):
    """ função que dado um numero calcula o fatorial deste numero;int-->int"""
    fatorial = 1
    while n>0:
        fatorial = fatorial * n
        n =n - 1
    if n < 0:
        fatorial = "indefimido"
    return fatorial