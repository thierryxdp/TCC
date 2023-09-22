def retira_pontuacao (frase):
	'''
    função que substitui pontuação por espaço vazio
    str -> str
    '''
    frase2 = frase.replace(str(',','.'),' ')
    return frase2