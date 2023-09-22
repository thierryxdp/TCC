def conta_frases(texto):
	result = len( texto.replace(',',' ').replace('.',' ').replace('?',' ').split())
    return result