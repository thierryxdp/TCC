def conta_frases(texto):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	# retirar espaços
	texto_esp = str.strip(texto,' ')
	# dividir em palavras
	texto_dividido = str.split(texto_esp,' ')
	frase1 = str.split(texto_dividido,'.|\?|','...|!')                    
	# contar  quantas existem
	qtd = len(frase1)

	return qtd