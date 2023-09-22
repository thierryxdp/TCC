def retira_pontuacao (frase):
	'''
    função que substitui pontuação por espaço vazio
    str -> str
    '''
    b = ',.;!?-'
    i = indice
    if b[i] in str(frase):
        return frase.replace ('.',' ') and frase.replace (',',' ')