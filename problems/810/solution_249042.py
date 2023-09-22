def inverte (frase):

	#trocar pontuacao
	frase = frase.replace('...',' ')
	#trocar pontuacao
    frase = frase.replace('-',' ')
    #trocar pontuacao
    frase = frase.replace(':',' ')
    #trocar pontuacao
    frase = frase.replace(',',' ')
    #trocar pontuacao
    frase = frase.replace('.',' ')
    #trocar pontuacao
    frase = frase.replace('?',' ')
    #trocar pontuacao
    frase = frase.replace('!',' ')
	#inverte a frase
	frase = frase.reverse
	return frase