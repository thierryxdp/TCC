def fatorial(n):
    '''função que calcula o fatorial do número informado; int => int'''
    fat = 1
    while n>1:
        fat*=n
        n-=1
    return fat
    return s