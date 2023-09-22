def fatorial(n):
    ''' funcao que recebe um numero e retorna o fatorial dele
        sem usar a funcao factorial do modulo import
        int -> int'''
    i = 1
    while n > 1:
        i = i*n
        n = n+1
    return i