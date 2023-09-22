def uppCons(frase):
    """Dada uma frase de entrada, retorna a mesma frase com todas as consoantes em maiuscolo;
    str -> str"""
    
    i = 0
    novafrase = ''
    
    while i < len(frase):
        if frase[i] in "bcçdfghjklmnpqrstvwxz":
        	novafrase += str.upper(frase[i])
        elif frase[i] not in "bcçdfghjklmnpqrstvwxz":
        	nova frase += frase[i]
    	i += 1
	return novafrase