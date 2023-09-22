def retira_pontuacao(frase):
    '''Função que dada uma frase , retorne a mesma frase onde todos os caracteres
       de pontuação substituindo-lhes por espaço.
       str ---> str'''
	final = str.replace(frase,',',' ')
	final = str.replace(final,':',' ')
	final = str.replace(final,';',' ')
	final = str.replace(final,'.',' ')
	final = str.replace(final,'!',' ')
    final = str.replace(final,'?',' ')
    final = str.replace(final,'-',' ')
	return final