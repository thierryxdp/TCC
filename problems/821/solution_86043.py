def fatorial(numero):
    """dado um número, calcula e retorna o fatorial deste número; int -> int"""
    fatorial_zero = 1
    if numero == 0 or numero == 1:
        return fatorial_zero
   
    n = 1
    while numero > 1:
        n = n*numero*(numero-1)
        numero = numero - 2
    return n