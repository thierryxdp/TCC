def inverte (Frase):
    """Inverta a Frase da entrada, deixando todas as letras maisculas e minusculas e removendo todas as pontuações. """
    Frase1 = Frase.replace (',', ' ')
    Frase1 = Frase.replace ('.', ' ')
    Frase1 = Frase.replace (';', ' ')
    Frase1 = Frase.replace ('!', ' ')
	return Frase1