def fatorial(numero):
    '''
	função que dado um número, calcula o fatorial deste número;
    int -> int
    '''
    numero_fatorial = numero
	while numero != 1:
        numero_fatorial = numero_fatorial * (numero - 1)
        numero = numero - 1
    return numero_fatorial