def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=1
    x=0
    num=0

    while i<=n:
        x=n*i
        num=num+x
        n=n-1
        i=i+1
        
    return num