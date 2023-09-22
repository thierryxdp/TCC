def conta_frases(text):
    	"""Função que dado um texto(text) retorna o número de frases presentes nele. string --> int"""
        x = str.split(text,'...')
    	x = str.join('*',x)
    	x = str.split(x,'?')
    	x = str.join('*',x)
    	x = str.split(x,'!')
    	x = str.join('*',x)
    	x = str.split(x,'.')
    	x = str.join('*',x)
    	return (len(str.split(x,'*')))-1