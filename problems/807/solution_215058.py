def conta_frases(texto):
    '''Retorna o numero de frases de um texto'''
    #str -> int
    ponto = str.count(texto, '.')
    exclamacao = str.count(texto, '!')
    interrogacao = str.count(texto, '?')
    reticencias = str.count(texto, '...')
    if reticencias == 0:
    	return ponto + exclamacao + interrogacao
    else:
        return ponto + exclamacao + interrogacao - 2*reticencias