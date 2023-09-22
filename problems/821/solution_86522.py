def fatorial(num):
    ''' Essa função dado um numero, calcula o fatorial deste numero
    int -> int'''
     c = cont = 1
    while cont < num:
        cont += 1
        c *= cont
    return c