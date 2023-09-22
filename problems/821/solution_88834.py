def fatorial(n):
    '''dado um numero n int, calcula o fatorial'''
    valor=n
    while n>1:
        valor=valor*(n-1)
        n-=1
    return valor