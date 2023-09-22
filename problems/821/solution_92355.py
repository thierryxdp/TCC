def fatorial(n):
    """função que dado um número, calcula o fatorial deste número
    int -> int"""
    fatorial=1
    while n>1:
        fatorial*=n
        n-=1
    return fatorial