def conta_frases(texto):
	texto = texto.replace('...','/')
	texto = texto.replace('.','/')
	texto = texto.replace('!','/')
	texto = texto.replace('?','/')
	aux = texto.split('/')
	return len(aux)-1