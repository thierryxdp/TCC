def conta_frases(texto):
    
    numero_frases1 = str.find(texto, '...')
    numero_frases2 = str.find(texto, '?')
    numero_frases3 = str.find(texto, '?')
    

	return (numero_frases1 + numero_frases2 + numero_frases3)