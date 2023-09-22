def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=n-1
    x=n
    num=0
    
    while (i>0):
        y=x*i
        num=num+y
    	i=i-1
    return num