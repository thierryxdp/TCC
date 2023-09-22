def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=0
    y=n+1
    num=0
    
    while (i<y):
        numero=n-i
        x=numero*i
        num=num+x
    	i=i+1
    return num