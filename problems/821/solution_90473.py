def fatorial(n):
    '''função que dado um número (N), calcula o fatorial deste número; int -> int'''
    N=1
    while n>=1:
        if n>=1:
            N*=n
        n=n-1
    return  N