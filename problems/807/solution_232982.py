def conta_frases(frase):
    '''A função recebe um texto com múltiplos sinais de pontuação ('?', '!' '.' e '...') e
retorna o número de frases desse texto, as separando pelos sinais.
	string -> int'''
	e1 = frase.replace('?', '.')
	e2 = e1.replace('!', '.')
    e3 = e2.replace('...', '.')
    e4 = e3.split('.')
    e4.remove('')
    return len(e4)