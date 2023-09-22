def fatorial(n):
    '''Entre com um numero para ser retornado seu valor fatorial
    Int -> Int'''
    i=1
    x=n+1
    num=0
    
    lista=list(range(x))
     
    while (i<x):
        num=num+lista[i]
        i=i+1
    return num