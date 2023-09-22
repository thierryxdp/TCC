def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=0
    x=n
    num=0

    while i<=n:
        x=x*1
        num=num+x
        x=x-1
        i=i+1
        
    return num