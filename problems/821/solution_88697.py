def fatorial(numero):
    '''Recebe um número e retorna o valor fatorial.
    int -> int'''
    fat = 1
    i = 2
    while i <= numero:
        fat = fat*i
        i = i + 1
    return fat