def inverte (frase):

	#trocar pontuacao
	frase = frase.replace('...','')
	#trocar pontuacao
    frase = frase.replace('-','')
    #trocar pontuacao
    frase = frase.replace(':','')
    #trocar pontuacao
    frase = frase.replace(',','')
    #trocar pontuacao
    frase = frase.replace('.','')
    #trocar pontuacao
    frase = frase.replace('?','')
    #trocar pontuacao
    frase = frase.replace('!','')
	#inverte a frase
	
	return frase.reverse