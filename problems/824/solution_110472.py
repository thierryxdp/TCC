def uppCons(frase):
    """Dada uma frase de entrada, retorna a mesma frase com todas as consoantes em maiuscolo;
    str -> str"""
    
    i = 0
    novafrase = ''
    
    while i < len(frase):
    	if frase[i] in "cçdfghjklmnpqrstvwxz":
        	novafrase += (frase[i])
    	i += 0
	return novafrase