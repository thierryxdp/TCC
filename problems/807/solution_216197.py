def conta_frase(texto):
    '''Conta o número de frases presentes no texto recebido
    string-> int'''
    n1 = texto.count('.')
    n2 = texto.count('!')
    n3 = texto.count('?')
    n4 = texto.count('...')
	return n1 + n2 + n3 + n4