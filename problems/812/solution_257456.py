def retira_pontuacao(frase):
	frase = str.replace(frase, '-',' ')
	frase = str.replace(texto, ',',' ')
	frase = str.replace(texto, ':',' ')
	frase = str.replace(texto, ';',' ')
	frase = str.replace(texto, '.',' ')
	frase = str.replace(texto, '!',' ')
	frase = str.replace(texto, '?',' ')
	return frase