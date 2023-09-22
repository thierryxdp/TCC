def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
	s = frase
	semponto = s.translate(str.maketrans('', '', string.punctuation))
	return semponto