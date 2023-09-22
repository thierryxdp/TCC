def fatorial(numero):
    '''dado um numero, calcula o fatorial.
    int -> int'''
    i = 1
    valor = 1
    while i <= numero:
        valor = valor * i
        i = i + 1 
    return valor