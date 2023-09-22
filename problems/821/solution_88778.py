def fatorial(n):
    '''Função que recebe um número n e retorna o valor do fatorial desse número(n>=0).
int --> int'''
    i = 1
    fatorial_final = 1
    while i <= n:
        fatorial_final = fatorial_final*i
        i = i+1
    return fatorial_final