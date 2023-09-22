def conta_frases(texto):
    """Esta função conta a quantidade de palavras em uma frase 
	str -> str """

	# retirar espaços
	texto_esp = str.strip(texto,' ')
	#trocar pontuacao
	texto_dividido1 = texto_esp.replace('&','.')
	#trocar pontuacao
	texto_dividido2 = texto_esp.replace('&',':')
	#trocar pontuacao
	texto_dividido3 = texto_esp.replace('&','...')
	#trocar pontuacao
	texto_dividido3 = texto_esp.replace('&','!')
	#trocar pontuacao
	texto_dividido4 = texto_esp.replace('&','?')
	# contar  quantas existem
	qtd = texto_dividido.count ( '&')

	return qtd