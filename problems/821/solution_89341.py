def fatorial (numero):
    """dado um numero, calcula o fatorial desse numero;
    int->int"""
    aux=1
    while numero >= 1:
        aux=aux*numero
        numero=numero-1
    return aux