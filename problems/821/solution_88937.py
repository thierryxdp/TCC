def fatorial(numero):
    """Funcao que dado um numero de entrada,
    retorne seu fatorial;
    int -> int"""
    contador=1
    acumulador=[numero]
    while contador<numero:
        acumulador=[acumulador[0]*(numero-contador)]
    return acumulador[0]