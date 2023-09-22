def retira_pontuacao(frase):
	'''Esta função retira determinadas pontuações de uma frase
   string -> string''' 
    if ':' in frase:
	frase = frase.replace(':', ' ')
	if ';' in frase:
	frase = frase.replace(';', ' ')
	if '.' in frase:
	frase = frase.replace('.', ' ')
	if '!' in frase:
	frase = frase.replace('!', ' ')
	if '-' in frase:
	frase = frase.replace('-', ' ')
	if ',' in frase:
	frase = frase.replace(',', ' ')
	if '?' in frase:
	frase = frase.replace('?', ' ')
	return frase