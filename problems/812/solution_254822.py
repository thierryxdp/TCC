def retira_pontuacao(frase):
'''Função que substitui todos os caracteres de pontuacao de uma frase dada por espaço.
 str-->str'''
	return frase.replace('.',' ').replace('-',' ').replace(',',' ').replace(':',' ').replace(';',' ').replace('!',' ').replace('?',' ')