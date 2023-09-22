def fatorial(numero):
    resultado=numero
    while numero>numero-1:
        resultado=numero*(numero-1)
        numero-=2
    return resultado