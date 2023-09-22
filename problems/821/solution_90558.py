def fatorial(numero):
	''' função que calcula o fatorial de um número inteiro 
	int --> int'''
	ctd = 1
	fatorial = numero
	while ctd < numero:
		fatorial = fatorial * ctd
		ctd = ctd + 1
	return fatorial