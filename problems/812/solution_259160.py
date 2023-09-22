def retira_pontuacao(x):
    '''Retorna uma frase sem caracteres de pontuação.
    str -> str'''
    s = x
	out = s.translate(str.maketrans('', '', string.punctuation))
	return out