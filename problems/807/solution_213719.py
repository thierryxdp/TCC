def conta_frases(frases):
	''' '''
	interrogacao=frases.split("?")
	ponto=interrogacao.split(".")
	exclamacao=ponto.split("!")
	reticencias=exclamacao.split("...")
	lista_reticencias=list(reticencias)
	qnt_frases=len(lista_reticencias)
	return qnt_frases