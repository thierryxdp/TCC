def fatorial(n):
    '''dado um numero inteiro n, essa funçao calcula n!;
    int-->int'''
    i=0
    fatorial=1
    while i<n:
        fatorial=fatorial*(n-i)
        i=i+1
    return fatorial