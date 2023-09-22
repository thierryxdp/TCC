def fatorial(n):
    '''Função que calcula o fatorial de um número 
    int -> list '''
    prod = 1
    for c in range(n, 0, -1):
        prod *= c
    return prod