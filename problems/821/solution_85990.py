def fatorial(n):
    '''dado um número, calcula seu fatorial
    int ->int'''
    i =1
    fatorial =1
    while i <=n:
        fatorial =fatorial*i
        i =i+1
    return fatorial