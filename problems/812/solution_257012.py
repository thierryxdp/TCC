def retira_pontuacao(frase):
	txt=(frase)
    if srt.count(frase,".")>0:
        return txt.replace("."," ")