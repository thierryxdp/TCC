def fatorial(numero):
    contador = numero
    fatorial = 1
    while contador>0:
        fatorial = fatorial*contador
        contador -=1
    return fatorial