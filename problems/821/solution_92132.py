def fatorial(n):
    '''funcao que dado um numero calcule o fatorial'''
    fat=1
    f=n-1
    while n-f>n-1:
        fat=n*(f)
        f=f-1
    return fat