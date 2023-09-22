def retira_pontuacao(frase):
	final = str.replace(frase,',',' ')
	final = str.replace(final,':',' ')
	final = str.replace(final,';',' ')
	final = str.replace(final,'.',' ')
	final = str.replace(final,'!',' ')
    final = str.replace(final,'?',' ')
    final = str.replace(final,'-',' ')
	return final