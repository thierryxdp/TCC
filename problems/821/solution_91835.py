def reduz(ls, f, init):
    r = init
    for e in ls:
        r = f(r,e)
    return r

def fatorial(n):

    r = range(1,n+1)

    return reduz (r, lambda x,y: x*y, 1)