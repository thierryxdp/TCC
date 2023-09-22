def fatorial(n):
    return prod(range(1,n+1))
def reduz(ls,op,init):
    r=init
    for e in ls:
        r= op(r,e)
    return r