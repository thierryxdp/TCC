def retira_puntuacao(frase):
    """retira todas pontuacoes de uma frase
    str->str"""
    out = frase.translate(str.maketrans('', '', string.punctuation))
	print(out)