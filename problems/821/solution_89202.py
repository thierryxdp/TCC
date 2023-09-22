def fatorial (x):
    i=x-1
    fac = x
    while i>0:
        fac = fac*(x-i)
        i = (x-1)-1
    return fac