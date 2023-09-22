def fatorial(numero):
    '''funcao que calcula dado um numero
    o fatoral do proprio
    entrada: inteiro
    saida: inteiro
    '''
    while numero>0:
        fatorial= numero*(numero - 1)
        numero= numero -1
    return fatorial