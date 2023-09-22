def retira_pontuacao(frase):
    if '!' in frase:
		final = frase.replace('!', ' ')
    	return final
    if ',' in frase:
        final = frase.replace(',', ' ')
        final1 = final.replace('.', ' ') 
        final2 = final1.replace('-', ' ')
        return final2
    if '?' in frase:
        final = frase.replace('?', ' ')
        return final