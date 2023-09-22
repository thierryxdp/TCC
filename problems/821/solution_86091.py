def fatorial(numero):
    limitador=int(numero)
    while limitador !=1:
        numero= numero*(limitador-1)
        limitador -= 1
    return numero