def conta_frases(frase):
	"""função que retorna o numero de frases em um texto
    str --> int"""
    frase = frase.replace('.','*')
    frase = frase.replace('...','*')
    frase = frase.replace('?','*')
    frase = frase.replace('!','*')
    return frase.count('*')