def conta_frases(texto):
    '''Esta função conta a quantidade de frases de um
    determinado texto
    string -> int'''
	f1 = texto.split(’.’)
	f2 = texto.split(’!’)
	f3 = texto.split(’?’)
	f4 = texto.count(’...’)
	return (len(f1) - 2*f4) + len(f2) + len(f3) - 3