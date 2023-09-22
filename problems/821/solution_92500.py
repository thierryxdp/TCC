def fatorial(n):
    '''str-->str'''
    x=0
    f=n
    u=n-1
    while x<=n:
        f=f*(u)
        u-=1
        x+=1
    return f