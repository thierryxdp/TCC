def fatorial(n):
    '''funcao que dado um numero calcule o fatorial'''
    fat=n
    f=n-1
    while n-f<n:
        fat=fat*(f)
        f=f-1
    return fat