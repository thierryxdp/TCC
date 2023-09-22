def retira_pontuacao(x):
    '''Retorna uma frase sem caracteres de pontuação.
    str -> str'''
    import re
	s = x
	out = re.sub(r'[^\w\s]','',x)
    return out