def conta_frases(texto):
    """função que dado um texto retorna a quantidade de frases que ele contém; str-> int"""
    frases_separadaspto=texto.split('. ') 
    return len(frases_separadaspto)
	else:
    	frases_separadasexc=texto.split('! ') 
    	return len(frases_separadasexc)