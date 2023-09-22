def conta_frases(texto):
    
    numero_frases2 = str.count(texto, '.')
	numero_frases2 = str.count(texto, '!')
	numero_frases3 = str.count(texto, '?')
	numero_frases4 = str.count(texto, '...')

	return (numero_frases2 + numero_frases3 + numero_frases4)