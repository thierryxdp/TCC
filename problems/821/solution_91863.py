def fatorial(numero):
    '''retorna o fatorial do numero dado
    int -> int'''
    multi = numero
    while numero>0:
            if numero>1:
                a = numero-1
                multi = multi*a
                numero -= 1
            else:
                numero -=1
    return multi