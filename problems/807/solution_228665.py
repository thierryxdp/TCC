def conta_frases(frase):
    count=0
    for i in range (0, len(frase)):        
        if frase[i] in (".") and frase[i+1] in (".") and frase[i+2] in ("."):
            count = count + 1
            i= i + 2
    	elif frase[i] in ("!", "?","."):  
        	count = count + 1  
    return count