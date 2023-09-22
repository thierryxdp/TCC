def conta_frases(texto):
    
    numero_frases2 = str.find(texto, '!')
	numero_frases3 = str.find(texto, '?')
	numero_frases4 = str.find(texto, '...')
	numero_frases1 = str.find(texto, '.')
	num_total = numero_frases1 + numero_frases2 + numero_frases3 + numero_frases4


    
    return (num_total)