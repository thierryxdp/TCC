def retira_pontuacao(frase):
	""" Esta função tira a pontuação das frases
	str -> str"""
	
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
    # contar  quantas existem
    qtd = frase