def fatorial(numero):
    i=0
    while numero!=i:
        numero = numero *(numero-i)
    i+=1
    return numero