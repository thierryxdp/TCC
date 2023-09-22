def uppCons(texto):
    """ A função retorna uma strig de texto
    com todas as suas consoantes maiúsculas.
    	str -> str """
    
    i = 0
    texto_novo = ''
    while i < len(texto):
        letra = texto[i]
        
        if letra.lower() in 'bcdfghjklmnpqrstvwxyz':
        	letra = str.upper(letra)
            
		texto_novo+=letra
        i = i + 1
	return texto_novo