def fatorial(n):
    '''funcao que dado um numero calcule o fatorial'''
    f=n-1
    while n-f>0:
        fat=fat*(f)
        f=f+1
    return fat