def fatorial(numero):
    """Funcao que dado um numero de entrada,
    retorne seu fatorial;
    int -> int"""
    contador=1
    acumulador=(numero)
    while contador<numero:
        acumulador=acumulador*(numero-contador)
        contador+=1
    return acumulador