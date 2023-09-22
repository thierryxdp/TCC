def conta_frases(texto):
    """funcao que conta o numero de frases no texto, sendo cada frase terminada com um ponto"""
	"""str->int"""
    ponto=str.count(texto,'.')
    reticencias=str.count(texto,'...')
    interrogacao=str.count(texto,'?')
    exclamacao=str.count(texto,'!')
    return -3*reticencias+reticencias+interrogacao+exclamacao