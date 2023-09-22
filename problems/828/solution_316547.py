def primo(numero):

	"""Recebe um numero e retorna se é um numero primo
	ou não; int-> bool."""
    for i in range (2,numero-1):
        if numero % i == 0:
            return False
        else:
			return True