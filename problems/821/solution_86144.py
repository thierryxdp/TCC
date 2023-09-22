def fatorial(n):
    '''função que calcula o fatorial do número (n) dado; int -> int'''
    i = 2
    fat = 1
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat