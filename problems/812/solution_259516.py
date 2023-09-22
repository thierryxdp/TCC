def retira_pontuacao(frase):
    if '!' in frase:
		final = frase.replace('!', ' ')
    	return final
    if ',' in frase:
        final = frase.replace(',', ' ')
        final1 = final.replace('.', ' ') 
        return final1
    if '?' in frase:
        final = frase.replace('?', ' ')
        return final