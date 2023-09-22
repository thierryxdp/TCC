def fatorial(n):
    ''' Funcao que dado um numero calcule seu fatorial
        : param n: int
        : return: int
    '''
    i=0
    fat=1
    while n-i>1:
        fat*=n-i
        i=i+1
    return fat