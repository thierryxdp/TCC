def retira_pontuacao(frase):
    pontuacoes=[".",",","–",":",";","!","?"]
    for x in frase:
        if x in pontuacoes:
            frase.remove(x)
	return frase