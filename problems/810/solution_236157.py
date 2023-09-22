def inverte(frase1):
	"""str=>str"""
	frase_nova=str.split(str.lower(retira_pontuacao(frase1))," "))
    str.join(" ",frase_nova[::-1]