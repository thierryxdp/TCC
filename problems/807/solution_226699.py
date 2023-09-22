def conta_frases(frases):
	'esta função determina a quantidade de frase atraves dos pontos'
	'str-->int'
	tres_ponto = str.count(frases, '...')
	ponto_final = str.count(frases, '.')
	ponto_exclamacao = str.count(frases, '!')
	ponto_interrogacacao = str.count(frases, '?')
	
	Q_frases = ponto_final + ponto_exclamacao + ponto_interrogacacao + tres_ponto 
	return Q_frases