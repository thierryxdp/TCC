def conta_frases(texto):
    '''Esta função conta a quantidade de frases de um
    determinado texto
    string -> int'''
	f1 = texto.replace(’.’)
	f2 = texto.replace(’!’)
	f3 = texto.replace(’?’)
	f4 = texto.count(’...’)
	return (len(f1) - 2*f4) + len(f2) + len(f3) - 3