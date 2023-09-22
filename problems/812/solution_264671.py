def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
	original = "string. With. Punctuations!?"
	semponto = original.translate(str.maketrans('', '', string.punctuation))
	return semponto