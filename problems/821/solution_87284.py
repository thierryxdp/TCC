def fatorial (numero):
    fatorial = numero
	while numero > 1:
        fatorial = fatorial * (numero - 1)
        numero -= 1
	return fatorial