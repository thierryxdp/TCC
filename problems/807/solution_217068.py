def conta_frases(frases):
    frases = str.replace(frases,'...','.')
	i = str.count(frases,'?')
	i = i + str.count(frases,'!')
	i = i + str.count(frases,'.')
    return i