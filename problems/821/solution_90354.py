def fatorial(numero):
    i=1
    while numero>i:
        numero = numero *(numero-i)
    i+=1
    return numero