def retira_pontuacao(frase):
	txt=(frase)
    if str.count(frase,".")>0:
        return txt.replace("."," ")