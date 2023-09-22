def fatorial(numero):
    """ função que dado um número, retorna o cálculo do fatorial desse número; 
    int-->int."""
    fatorial = 1
    if numero<2:
        return 1
    while numero >= 1:
        fatorial = fatorial*numero
        numero = numero-1
    return fatorial