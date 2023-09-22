def conta_frases(frase):
	"""função que retorna o numero de frases em um texto
    str --> int"""
    frase = frase.replace('.','x')
    frase = frase.replace('...','x')
    frase = frase.replace('?','x')
    frase = frase.replace('!','x')
    return frase.count('x')