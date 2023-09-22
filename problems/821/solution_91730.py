def fatorial (n):
    '''função em que dado um número (n) calcule o fatorial desse número;
    int -> int'''
    i=1
    f=1
    while i<=n:
        f=f*i
        i=i+1
    return f