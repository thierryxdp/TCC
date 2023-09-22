def conta_frases(frase):
	'''Essa funcao conta frases. Recebe como parametro uma stringque considera como separador de frase 'ponto final', 'exclamacao','interrogacao', e 'reticencias' '''
    frase.split('.')
    frase.split('!')
    frase.split('?')
    frase.split('...')
    return len(frase)