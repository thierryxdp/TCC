def fatorial(numero):
    """função que dado um número,calcule o fatorial desse numero;
    int -> int"""
    acumulador = 1
    proximo = numero
    while proximo > 1 :
        acumulador = acumulador*proximo
        proximo = proximo - 1
    return acumulador