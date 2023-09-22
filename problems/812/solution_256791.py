def retira_pontuacao(frase):
    
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
    import string
    pont = string.punctuation
	for c in pont:
    	frase = frase.replace(c, "")