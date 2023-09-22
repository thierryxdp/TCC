def fatorial(numero):
    i=numero
    while i>0:
        numero = numero*(numero-1)
    i = i-1
    return numero