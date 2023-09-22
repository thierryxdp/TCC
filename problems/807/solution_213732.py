def conta_frases(frases):
	'''Função que conta o número de frases que aparecem em um texto
    str->int'''
	sp_frases=frases.replace("!",".")
	sp_frases=sp_frases.replace("?",".")
	sp_frases=sp_frases.replace("...",".")
	split_frases=sp_frases.split(".")
	lista_frases=list(split_frases)
	qnt_frases=len(lista_frases)
	return qnt_frases - 1