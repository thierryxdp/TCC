def conta_frases(frases):
    '''Esta função conta a quantidade de frases de um
    determinado texto
    string -> int'''
	frase1 = frases.replace(’.’)
	frase2 = frases.replace(’!’)
	frase3 = frases.replace(’?’)
	frase4 = frases.count(’...’)
	return (len(f1) - 2*f4) + len(f2) + len(f3) - 3