def retira_pontuacao (frase):
	'''
    função que substitui pontuação por espaço vazio
    str -> str
    '''
    frase2 = frase.replace(',',' ')
    frase3 = frase2.replace('.',' ')
    frase4 = frase3.replace('!',' ')
    frase5 = frase4.replace('?',' ')
    frase6 = frase5.replace('-',' ')
    return frase6