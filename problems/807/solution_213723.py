def conta_frases(frases):
	''' '''
	sp_frases=frases.split(". |! |? |...", frases)
	lista_frases=list(sp_frases)
	qnt_frases=len(lista_frases)
	return qnt_frases