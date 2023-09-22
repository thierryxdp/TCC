def fatorial(n):
    '''Funcao recebe um numero e retorna o fatorial desse mesmo numero
int -> int'''
    acumulador = 1
    decrescente = n 
    while (decrescente != 0):
        acumulador = acumulador * decrescente
        decrescente = decrescente - 1
    return acumulador