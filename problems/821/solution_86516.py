def fatorial(numero):
    fator=numero-1
    while fator>1:
        numero=fator*numero
        fator=fator-1
    return numero