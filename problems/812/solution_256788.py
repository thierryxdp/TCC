def retira_pontuacao(frase):
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
    pont = str.punctuation
	for c in punct:
    	frase = frase.replace(c, "")