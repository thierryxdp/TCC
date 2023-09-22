def fatorial(n):
    '''Calcula o fatorial de um número;
    int -> int'''
    if n == 0:
        return 1
    fatorial = 1
    for numero in range(1, n + 1):
    	fatorial *= numero
    return fatorial