def fatorial(numero):
    '''dado um numero retorna o seu fatorial
    int->int'''
    i=0
    fator=1
    while i<numero:
        fator*=(numero-i)
    	i+=1
    return fator