def conta_frases(texto):
    '''
    Função que recebe um texto e retorna quantas frases existem no texto.
	str -> int
    '''
    frases = texto.replace('!','.').replace('?', '.').replace('...', '.')
    frases = frases.split('. ')
    return len(frases)