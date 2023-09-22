def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    frases = texto.split('.' or '...' or '!' or '?')
    qnt = len(frases)
	return qnt