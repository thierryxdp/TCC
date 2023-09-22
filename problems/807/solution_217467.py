def conta_frases(frases):
    """Conta o número de frases que aparecem em um texto; str, ->int """"
    frases = str.replace(frases,'...','.')
	i = str.count(frases,'?')
	i = i + str.count(frases,'!')
	i = i + str.count(frases,'.')
    return i