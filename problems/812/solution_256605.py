def retira_pontuacao(frase):
	"""funcao que substitui pontuacoes por espacos
    list -> list"""
    s=(frase)
    if str.index((frase),"?"):
    	return s.replace("?"," ")
    if str.index((frase),"."):
    	return s.replace("."," ")
    if str.index((frase),","):
    	return s.replace(","," ")