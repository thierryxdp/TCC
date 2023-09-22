def fatorial(n):
    '''Função que calcula o fatorial de um número
    float -> float'''
    f=1
    while n>0:
    	f=f*n
        n=n-1
    return f