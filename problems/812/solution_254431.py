def retira_pontuacao(frase):
    '''Função que substitui todos os caracteres de pontuacao por espaço.
       str-->str'''
	return frase.replace('.' or ',' or '!' or ',' or '-' or':' or ';'or'?',' ')