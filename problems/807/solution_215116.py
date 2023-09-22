def conta_frases(frase):
    '''
    dado um texto retorna o numero de frases 
    '''
    if  '...' in frase:
    	return frase.count('!')+frase.count('?')+frase.count('...')+ frase.count('.')-frase.count('...')*3
    else:
        return frase.count('!')+frase.count('?')+ frase.count('.')