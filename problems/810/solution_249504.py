def retira_pontuacao(frase):
    '''inverte a ordem das palavras, retira as letras maiúculas e a pontuação. 
    str->str'''
	str.join(frase," ")
	return upper(str.reverse(frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")))