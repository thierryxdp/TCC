def fatorial(n):
    '''Dado um numero n, retorna a fatorial deste numero.
    int -> int'''
    i=0
    jota=n
    while jota>i:
        n=(n)*(n-i)
        i=i+1
        return n