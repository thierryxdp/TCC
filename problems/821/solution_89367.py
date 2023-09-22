def fatorial (n):
    '''
    	essa função recebe um número e retorna o cálculo do seu fatorial
        int-->int
    '''
    i = 0
    x = 0
    n = range(1, n+1)
    while i < len(n):
        x=x*n[i]
        i = i+1
    return x