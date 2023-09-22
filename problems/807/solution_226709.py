def conta_frases(frases):
	'esta função determina a quantidade de frase atraves dos pontos'
	'str-->int'
	frase = str.replace(frases,'...','.')
	ponto_final = str.count(frase, '.')
	ponto_exclamacao = str.count(frase, '!')
	ponto_interrogacacao = str.count(frase, '?')
	Q_frases1 = ponto_final + ponto_exclamacao + ponto_interrogacacao  
	return Q_frases1