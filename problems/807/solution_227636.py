def conta_frases(texto):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	# retirar espaços
	
	# dividir em palavras
	texto_dividido = str.split(texto,'.|\|...|!')
	# contar  quantas existem
	qtd = len(texto_dividido)

	return qtd