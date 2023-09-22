def fatorial(n):
    '''str-->str'''
    x=1
    f=n
    i=n
    while x<i:
        f=f*(n-1)
        n-=1
        x+=1
    return f