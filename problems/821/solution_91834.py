def fatorial(n):

    r = range(1,n+1)

    return reduz (r, lambda x,y: x*y, 1)