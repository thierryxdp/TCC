def uppCons(frase):
    """Retorna a mesma frase colocada com as consoantes em maiúsculo
       string -> string"""
    frase = list(frase)
    consoantes = ("bcdfghjklmnpqrstvwxyzç")
    i = 0
    
    while i < len(frase):     
    
    	if frase[i] in consoantes:
        	frase[i] = frase[i].upper()
            
        i += 1
	return "".join(frase)