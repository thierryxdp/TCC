def retira_pontuacao (frase):
	'''
    função que substitui pontuação por espaço vazio
    str -> str
    '''
    frase2 = frase.replace(',',' ')+frase.replace('.',' ')
    return frase2