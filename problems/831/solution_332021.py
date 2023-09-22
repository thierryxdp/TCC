def lingua_p(palavra)
	"""."""
	traduzido = ''
	for letra in palavra
		if letra in 'aáâeéêiíoóôuú'
			traduzido += letra+'p'+letra
		else:
			traduzido += letra

	return traduzido