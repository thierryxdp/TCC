def retira_pontuacao(s):
    '''retira a pontuação'''
    import re

	s = str
	out = re.sub(r'[^\w\s]','',s)
	return out