def retira_pontuacao (frase):
    '''substitui a pontuação de uma frase por espaço.
    str -> str'''
    
	punct = str.punctuation
	for c in punct:
   		s = s.replace(c, "")
	return s