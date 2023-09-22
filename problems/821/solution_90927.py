def fatorial (n):
    '''função que dado um número (n) retorna o seu fatorial;
    int->int'''
    sub=1
    while n>=1:
        sub=sub*n
        n=n-1
    sub+=1
    return sub