def inverte(frase):
    '''
    
    '''
    
    if '-' or ',' or '.' in frase:
		virgula = frase.replace(',', ' ')
	ponto_final = virgula.replace('.', ' ')
    return reversed(ponto_final)
    
    if '?' in frase:
        	virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    return reversed(ponto_interrogacao)
    
    if '!' in frase:
        	virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    	return reversed(ponto_exclamacao)