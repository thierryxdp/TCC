def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    x = 0
    x = x + list.count(texto, '.')
    x = x + list.count(texto, '!')
    x = x + list.count(texto, '...')
    x = x + list.count(texto, '?')
	return x