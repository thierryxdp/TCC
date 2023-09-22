def fatorial(n):
    """função que recebe um número n e calcula o fatorial
    deste número.
    int -> int"""

    i = 1
    acumulador = 1

    while i <= n:
        acumulador = acumulador * i
        i = i + 1
    
    return acumulador