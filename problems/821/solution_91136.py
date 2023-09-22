def fatorial(n):
    '''retorna o fatorial do numero determinado
    int -> int'''
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact