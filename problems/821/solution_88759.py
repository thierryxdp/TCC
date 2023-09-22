def fatorial(numero):
    contador=0
    resultado=numero
    while numero>0:
        resultado=numero*(numero-1)
        numero-=1
    return resultado