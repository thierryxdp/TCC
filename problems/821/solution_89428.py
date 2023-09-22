def fatorial(numero):
    '''dado um numero(numero), retorna o fatorial do mesmo; int -> int'''
    multiplo = numero
    numerox = 0
    while multiplo > 0:
        numerox = (multiplo) * (multiplo - 1)
        multiplo = multiplo - 1
    return numerox