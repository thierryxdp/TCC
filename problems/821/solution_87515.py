def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    i=1
    while n>i:
        fat=n
        fat=fat*(fat-i)
        i=i+1
    return fat-i