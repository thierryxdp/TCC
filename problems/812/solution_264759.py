def retira_pontuacao(frase):
    '''inverte a ordem das palavras, retira as letras maiúculas e a pontuação. str->str'''
	str.join(frase," ")
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
def inverte(frase):
    '''retorna  a frase invertida, sem letras maiúsculas. str -> str'''
    list_frase = str.split(retira_pontuacao(frase))
    list.reverse (list_frase)
    return str.lower(str.join(' ', list_frase))