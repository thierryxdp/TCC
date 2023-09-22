def conta_frases(frases):
    '''Esta função conta a quantidade de frases de um
    determinado texto
    string -> int'''
	f1 = frases.replace(’.’)
	f2 = frases.replace(’!’)
	f3 = frases.replace(’?’)
	f4 = frases.count(’...’)
	return (len(f1) - 2*f4) + len(f2) + len(f3) - 3