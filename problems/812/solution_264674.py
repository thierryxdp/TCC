def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
	s = frase
	out = re.sub(r'[^\w\s]','',s)
	returnout