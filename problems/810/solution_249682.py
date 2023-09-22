def inverte(frase):
  '''dada um frase, retorna a mesm frase de ordem inversa, sem letras maiúsculas e sem pontuação str->str'''
	str.join(frase," ")
	return frase.replace("-", " ").replace(",", " ").replace(":", " ").replace(";", " ").replace(".", " ").replace("?", " ").replace("!", " ")
def inverte(frase):
    '''retorna  a frase invertida, sem letras maiúsculas. str -> str'''
    list_frase = str.split(retira_pontuacao(frase))
    list.reverse (list_frase)
    return str.lower(str.join(' ', list_frase))