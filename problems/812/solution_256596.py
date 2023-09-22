def retira_pontuacao(frase):
	"""funcao que substitui pontuacoes por espacos
    list -> list"""
    s=(frase)
    return s.replace("!"," ") + s.replace(","," ")