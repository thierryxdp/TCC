def conta_frases(texto):
    '''Dado um texto, retorna o numero de frases nesse texto;
    string -> int'''
	ntexto = str.replace(texto, '...', '!')
    return str.count(ntexto, '.') + str.count(ntexto, '!') + str.count(ntexto, '?')