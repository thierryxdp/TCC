def conta_frases(texto):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	# retirar espaços
	texto_esp = str.strip(texto,' ')
	# dividir em palavras
	texto_dividido = str.split(texto_esp,'.|\|...|!')
	# contar  quantas existem
	qtd = list.count(texto_dividido)

	return qtd