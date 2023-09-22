def conta_frases(texto):
    
    i = 0
    
    numero_frases1 = str.count(texto, '...')
    i = i + numero_frases1
    numero_frases2 = str.count(texto, '?')
    i = i + numero_frases2
    numero_frases3 = str.count(texto, '!')
    i = i + numero_frases3
    numero_frases4 = str.count(texto, '.')
    i = i + numero_frases4
    

	return (i)