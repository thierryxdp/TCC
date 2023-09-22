def uppCons(frase):
    """Dada a frase de entrada, retorna a mesma frase com todas as consoantes em maiuscolo;
    str -> str"""
    
    i = 0
    novafrase = ''
    
    while i < len(frase):
    	if frase[i] in "cçdfghjklmnpqrstvwxyz":
        	novafrase += str.upper(frase[indice])
    	i+= 0
	return novafrase