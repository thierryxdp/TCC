def fatorial(n):
    '''
    função que dado um número n, calcula o fatorial desse número
    int->
    '''   
    anterior = n-1
    while n >= 2:
        n = n*anterior
    n -= 1
    return n