def conta_frases(frase):
    '''
    '''
    if  '...' in frase:
    	return frase.count('!')+frase.count('?')+frase.count('...')+ frase.count('.')-frase.count('...')*3
    else:
        return return frase.count('!')+frase.count('?')+ frase.count('.')