def retira_pontuacao(frase):
    """Funçao que me dada uma frase irá me retornar a mesma frase mas sem nenhuma pontuação contida nela, deixando 
apenas espaços nos lugares das pontuações. str>str"""
	frase = frase
	frase = frase.replace(',',' ')
	frase = frase.replace('.',' ')
	frase = frase.replace('!',' ')
	frase = frase.replace('?',' ')
	frase = frase.replace(':',' ')
	frase = frase.replace(';',' ')
	frase = frase.replace('-',' ')
	return frase