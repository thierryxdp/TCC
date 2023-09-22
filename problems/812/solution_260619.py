def retira_pontuacao(frase):
    if '!' in frase:
    	a = str.replace(frase,'!',' ')
    	return a
    if '.' in frase:
        b = str.replace(frase,'.',' ')
        return b