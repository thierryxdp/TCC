def fatorial(n):
    '''retorna o fatorial do número de entrada; int -> int'''

    fat = n    

    while n > 1:
        fat = fat*(n-1)
        n = n-1
    return fat