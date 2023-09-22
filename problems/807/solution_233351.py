def conta_frases(texto):
    '''Conta o numero de frases que aparecem no texto.
    str-->int'''
    qnt = 0
    pontuacao = '!' or '?' or '...' or ':' or '.'
    frases = texto.split(pontuacao)
	x = list.count(frases)
    return x