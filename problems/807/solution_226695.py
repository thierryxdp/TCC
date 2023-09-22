def conta_frases(frases):
	'esta função determina a quantidade de frase atraves dos pontos'
	'str-->int'
    tres_ponto = str.count(frases, '...')
	frase = str.strip(frases,'...')
	ponto_final = str.count(frase, '.')
	ponto_exclamacao = str.count(frase, '!')
	ponto_interrogacacao = str.count(frase, '?')
	
	Q_frases = ponto_final + ponto_exclamacao + ponto_interrogacacao + tres_ponto 
	return Q_frases