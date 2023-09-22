def fatorial(n):
    '''int -> int'''
    i=1
    x=n-i
    y=n
    while x>1:
        y=y*x
        x=x-1
    return y