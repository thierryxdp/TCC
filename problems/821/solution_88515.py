def fatorial(n):
    '''função que dada um número calcula o fatorial desse número:int->int'''
    fat = 1 
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
    return fat