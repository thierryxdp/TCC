def fatorial(n):
    y=n
    x=n-1
    while y>1:
        n=n*x
        x=x-1
        y=y-1
    return n