def fatorial(n):
    '''Funçao que dado um numero na entrada n calcula e retorna o fatorial
    int -> int'''
    fatorial = 1 
    while n >= 1:
        fatorial = fatorial + n
        n = n - 1
    return fatorial