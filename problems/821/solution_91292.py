def  fatorial(numero):
    '''funçao  calcula  um  numero  inteiro qualquer'''
    'int--> int'

    i = 1
    fator= numero

    while i < numero:
        fator = fator * i
        i += 1

    return fator