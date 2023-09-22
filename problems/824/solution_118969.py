def uppCons(frase):
    """Funcao que retorna a frase de entrada com
    todas as consoantes maiusculas"""
	proximo = 0
    while proximo < len(frase):
        if frase[proximo] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[proximo])
    	proximo = proximo + 1
    	return frase