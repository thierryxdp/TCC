def fatorial(n):
    '''Calcula o fatorial de n (n>0);
       int -> int'''
    contador = n
    acumulador = 1
    while contador > 1:
        acumulador = acumulador*contador
        contador = contador - 1
    return acumulador