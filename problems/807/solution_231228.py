def conta_frases(f):
    ''' Retorna o número de frases de um texto f
    str -> int'''
    if f.count('.')==0:
    	return f.count('.')+f.count('!')+f.count('?')+f.count('...')
    else:
        return f.count('.')-f.count('...')*3+f.count('!')+f.count('?')+f.count('...')