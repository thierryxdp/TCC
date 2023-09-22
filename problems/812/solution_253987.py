import string
def retira_pontuacao(frase):
    pontuacao = string.punctuation
    for i in pontuacao:
		frase = frase.replace(i, " ")
		return frase