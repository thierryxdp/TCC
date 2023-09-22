def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
	s = frase
	out = ''.join([i for i in s if i not in str.punctuation])
	return out