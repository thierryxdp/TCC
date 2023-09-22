def soma_h(n):
    ''' dado um numero natural n, a funcao retornara a soma 
    h = 1 +1/2+1/3+...+1/n'''
    h = 0
    for i in range(1,n+1):
        h = h + 1/i
    return round(h,2)