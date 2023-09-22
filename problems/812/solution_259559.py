"""Retorna a frase sem pontuação:
str->str"""
def retira_pontuacao(frase):
    if '.' or ',':
    	frase = str.split(frase, "." or ',')
    	frase = str.join(" ", frase)
    	return frase
    elif '.':
        frase = str.split(frase, "!")
    	frase = str.join(" ", frase)
    	return frase