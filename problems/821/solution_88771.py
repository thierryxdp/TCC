def fatorial(numero):
    resultado=numero
    while numero>1:
        resultado=numero*(numero-1)
        numero-=1
    return resultado