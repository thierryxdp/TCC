def conta_frases(texto):
   
    x = texto.split('.')
	y = texto.split('!)
    z = texto.split('?)
    w = texto.split('...')
    
	return len(x) + len(y)