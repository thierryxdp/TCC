def carros(x,y=5):
    ''' função que calcula o número de carros necessários para transportar x pessoas'''
    N=x/y
    n=x//y
    if(N>n):
        return n+1
    else:
        return n