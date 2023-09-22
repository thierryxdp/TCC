def fatorial(n):
    i=1
    x=n
    while n!=1 and n>0:
        x=x*(i)
        i=i+1
        n=n-1
    if n==0:
        return 0
    if n<0:
        return False
    return x