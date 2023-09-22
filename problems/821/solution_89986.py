def fatorial(n):
    '''Funao recebe um numero e retorna o fatorial do mesmo, int -> int'''
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i = i + 1
        
    return fat