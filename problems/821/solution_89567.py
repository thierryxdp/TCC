def fatorial(n):
    ''' funcao recebe um numero e devolve o seu fatorial,int-->int'''
    proximo= (n-1)
    while n>1:
        n*proximo
    proximo= proximo-1
    return n