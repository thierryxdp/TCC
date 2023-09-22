def contando_reticencias (a,d):
	'''a cada d, subtrai 3 em a'''
	return a-(3*d)

def conta_frases(texto):
    '''retorna o numero de frases que aparecem em um texto, sendo cada frase 
    terminada com (./!/?/...) str -> int'''
    a = str.count(texto, '.')
    b = str.count(texto, '!')
    c = str.count(texto, '?')
    d = str.count(texto, '...')
    return contando_reticencias(a,d)+b+c+d