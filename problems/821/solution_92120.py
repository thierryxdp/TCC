def fatorial(n):
    '''funcao que dado um numero calcule o fatorial'''
    fat=0
    i=n-1
    while n-i>0:
        fat=fat*(n-i)
    return fat