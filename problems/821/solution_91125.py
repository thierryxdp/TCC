def fatorial(numero):
    ''' funçaõ que dado um número, calcula o fatorial do mesmo.
    int -> int
    '''
    i = 1
    fatorial = numero
    while i < numero:
        fatorial = fatorial * i
        i = i + 1
    return fatorial