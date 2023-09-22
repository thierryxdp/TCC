def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=1
    num=0

    while i<=n:
        num=num+(n*i)
        n=n-1
        i=i+1
        
    return num