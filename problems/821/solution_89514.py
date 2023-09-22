def fatorial(numero):
    '''funcao que calcula dado um numero
    o fatoral do proprio
    entrada: inteiro
    saida: inteiro
    '''
    auxiliar= 1
    while numero>1:
        fatorial= numero*(numero - 1)
        auxiliar= auxiliar*fatorial
        numero= numero -2
    return auxiliar