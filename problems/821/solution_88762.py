def fatorial(numero):
    resultado=numero
    while numero>0:
        numero -= 1
        resultado*=numero
    return resultado