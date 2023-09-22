def retira_pontuacao(frase):
    '''Função que dada uma frase, retorna a frase sem as pontuações; str->str'''
    import string
    p = string.punctuation
    for c in p:
    	frase = frase.replace(c, " ")
	return frase