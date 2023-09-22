def fatorial(numero):
    contador = numero
    if numero == 0:
		return 1
    elif contador > 0:
		while contador>0:
			numero = numero*(numero-1)
            contador = contador - 1
        return numero