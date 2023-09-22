def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    qnt = 0
    frases = texto.split('!')
    frases = texto.split('.')
    frases = texto.split('...')
    frases = texto.split('?')
    
	x = list.count(frases)
    return x