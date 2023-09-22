def fatorial(numero):
    '''
	função que dado um número, calcula o fatorial deste número;
    int -> int
    '''
	while numero != 1:
        fatorial = numero * (numero - 1)
    numero = numero - 1
    return fatorial