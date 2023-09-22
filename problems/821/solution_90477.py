def fatorial(n):
    '''função que calcula o fatorial de um numero n
    int->int'''
    i=1
    fat=1
    while (i<=n):
        fat=fat*(i)
        i=i+1
    return fat