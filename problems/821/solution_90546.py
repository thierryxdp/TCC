def fatorial(numero):
    ''' função que ao receber um número retorna o seu fatorial
    	int ---> int '''
    a = 1
    b = 0
    while a < numero + 1:
        b = b+1
        fatorial2 = b * (b + 1)
        a += 1
    return fatorial2