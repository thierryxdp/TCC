def fatorial(n):
    '''Função que dado um número, calular seu fatorial, int -> int'''
    fat = 1
    while (n>=1):
        fat = fat*n
        n = n - 1
    return fat