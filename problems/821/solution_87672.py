def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=0
    x=0
    y=n
    num=0
    
    while (i<=n):
        y=n-i
        x=y*i
        num=num+x
    	i=i+1
    return num