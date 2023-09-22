def fatorial(numero):
    '''função que dado um numero inteiro, calcula o fatorial 
    deste numero
    int->int'''
    numero1 = 1
    fator= 1
    while fator <= numero:
        numero1 = numero1 * fator
		fator = fator + 1
    return numero1