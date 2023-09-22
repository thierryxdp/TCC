def fatorial(n):
    '''dado um número(n), retorna o fatorial desse número; int -> int'''
    f = n
    contador = 1
    while(n-contador) > 1:
        f = f * (n-contador)
        contador = contador + 1
    return f