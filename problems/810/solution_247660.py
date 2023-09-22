def inverte(frase):
    '''
    
    '''
    
    if '-' or ',' or '.' in frase:
		virgula = frase.replace(',', ' ')
	ponto_final = virgula.replace('.', ' ')
    		return str.join(reversed(str.split(ponto_final)))
    
	virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    elif '?' in frase:
    	return str.join(reversed(str.split(ponto_interrogacao)))
    
	virgula = frase.replace(',', ' ')
    ponto_final = virgula.replace('.', ' ')
    ponto_interrogacao = ponto_final.replace('?', ' ')
    ponto_exclamacao = ponto_interrogacao.replace('!', ' ')
    elif '!' in frase:
    	return str.join(reversed(str.split(ponto_exclamacao)))