def retira_pontuacao(frase):
	'''Esta função retira determinadas pontuações de uma frase
   string -> string''' 
	frase = frase.replace(':', ' ')
	frase = frase.replace(';', ' ')
	frase = frase.replace('.', ' ')
	frase = frase.replace('!', ' ')
	frase = frase.replace('-', ' ')
	frase = frase.replace(',', ' ')
	frase = frase.replace('?', ' ')
	return frase