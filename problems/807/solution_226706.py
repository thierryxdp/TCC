def conta_frases(frases):
	'esta função determina a quantidade de frase atraves dos pontos'
	'str-->int'
	f = frases
	F = '...'
	if F in f:
		tres_ponto = str.count(frases, '...')
		frase = str.strip(frases,'...')
		ponto_final = str.count(frase, '.')
		ponto_exclamacao = str.count(frase, '!')
		ponto_interrogacacao = str.count(frase, '?')
		Q_frases = ponto_final + ponto_exclamacao + ponto_interrogacacao + tres_ponto 
		return Q_frases
	else :
		tres_ponto = str.count(frases, '...')
		ponto_final = str.count(frases, '.')
		ponto_exclamacao = str.count(frases, '!')
		ponto_interrogacacao = str.count(frases, '?')
		Q_frases1 = ponto_final + ponto_exclamacao + ponto_interrogacacao + tres_ponto 
		return Q_frases1