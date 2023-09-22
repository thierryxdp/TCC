def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
    import re
	s = frase
	out = re.sub(r'[^\w\s]','',s)
	return out