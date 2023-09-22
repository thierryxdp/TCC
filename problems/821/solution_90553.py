def fatorial(numero):
    ''' função que ao receber um número retorna o seu fatorial
    	int ---> int '''
    a = 1
    while a < numero + 1:
        fatorial2 = numero * (numero-1)
        numero -= 1
        a += 1
    return fatorial2