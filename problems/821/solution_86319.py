def fatorial (numero):
    '''Funçao que, dado um numero, retorna o fatorial deste numero.
    int -> int'''

    fat = 1
    i = 1
    while i <= numero:
        fat = fat*i
        i = i + 1
    return fat