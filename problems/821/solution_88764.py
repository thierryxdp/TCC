def fatorial(numero):
    resultado=numero
    while numero>0:
        resultado=numero*(numero-1)
        numero-=2
    return resultado