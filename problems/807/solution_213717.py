def conta_frases(frases):
	''' '''
	interrogacao=frases.split("?")
    ponto=frases.split(".")
    exclamacao=frases.split("!")
    reticencias=frases.split("...")
	lista_interrogacao=list(interrogacao)
    lista_ponto=list(ponto)
    lista_exclamacao=list(exclamacao)
    lista_reticencias=list(reticencias)
	qnt_frases=len(lista_interrogacao)+len(lista_ponto)+len(lista_exclamacao)+len(lista_reticencias)
	return qnt_frases