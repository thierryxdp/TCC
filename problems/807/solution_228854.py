def conta_frases(texto):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	#trocar pontuacao
	frase = frase.replace('.','&')
	#trocar pontuacao
	frase = frase.replace(':','&')
	#trocar pontuacao
	frase = frase.replace('...','&')
	#trocar pontuacao
	frase = frase.replace('!','&')
	#trocar pontuacao
	frase = frase.replace('?','%')
	# contar  quantas existem
	qtd = frase.count ( '&')

	return qtd