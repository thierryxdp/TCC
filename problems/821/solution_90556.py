def fatorial(numero):
    ''' função que ao receber um número retorna o seu fatorial
        int ---> int '''
    a = 1
    fator = numero
    while a < numero + 1:
        fatorial2 = numero * (fator-1)
        fator = numero
        a += 1
    return fatorial2