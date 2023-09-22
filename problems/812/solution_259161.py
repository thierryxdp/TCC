def retira_pontuacao(x):
    '''Retorna uma frase sem caracteres de pontuação.
    str -> str'''
    import string
	s = x
	punct = string.punctuation
	for c in punct:
    s = s.replace(c, "")
	return s