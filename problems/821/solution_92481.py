def fatorial(n):
    '''str-->str'''
    x=1
    f=n
    while x<n:
        f=f*(n-1)
        n-=1
        x+=1
    return f