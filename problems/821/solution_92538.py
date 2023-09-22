def fatorial(numero):
    if numero == 0:
		return 1
    elif numero > 0:
		while numero>0:
			numero = numero*(numero-1)
        return numero