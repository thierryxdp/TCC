def conta_frases(texto):
    '''Esta função conta o número de frases contida no texto
    inserido.
    str -> int'''
    
    frase1=str.count(texto,'.')
    frase2=str.count(texto,'!')
    frase3=str.count(texto,'?')
    frase4=str.count(texto,'...')
	quant_frase=frase1+frase2+frase3-2*frase4
	
	return quant_frase