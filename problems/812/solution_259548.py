"""Retorna a frase sem pontuação:
str->str"""
def retira_pontuacao(frase):
    if "!":
    	frase = str.split(frase, "!" and ",")
    	frase = str.join(" ", frase)
    	return frase