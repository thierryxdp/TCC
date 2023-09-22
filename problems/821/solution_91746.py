def fatorial(n):
    return prod(range(1,n+1)
def reduz(ls,op,init):
    r=init
    for e in ls:
        r= op(r,l)
    return r
def prod(ls):
    return reduz(ls, lambda x,y: x*y,1)