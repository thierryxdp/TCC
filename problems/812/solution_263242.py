def retira_pontuacao (frase):
	'''
    função que substitui pontuação por espaço vazio
    str -> str
    '''
    if str('?') in frase:
        return frase.replace('?',' ')
    if str('!') in frase:
        return frase.replace('!',' ')
    if str('?') in frase:
        return frase.replace('?',' ')
    if str('-') in frase:
        return frase.replace('-',' ')
    if str('.') in frase:
        return frase.replace('.',' ')
    	if str(',') in frase:
        	return frase.replace(',',' ')