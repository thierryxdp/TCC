def fatorial(n):
    """Função chamada fatorial, que dado um número, calcule o fatorial deste número."""
    i=1
    while(n > 0):
        i=(i*n)
        n-=1
    return i