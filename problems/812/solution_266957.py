def retira_pontuacao(s):
    '''retira a pontuação'''

	punct = string.punctuation
	for c in punct:
    	s = s.replace(c, "")
	return s