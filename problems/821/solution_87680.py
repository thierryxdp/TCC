def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=n-1
    num=0
    
    while (i!=0):
        x=n*i
        num=num+x
    	i=i-1
    return num