def fatorial(n):
    i=n
    res = 1
    while i>n:
        res*=i
        i-=1
        return res