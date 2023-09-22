def conta_frases(frase):
    count=0
    for i in range (0, len(frase)):
        if frase[i] in ("..."):
            count = count + 1
        	pass
    	elif frase[i] in ('!', "?" ,"."):  
        	count = count + 1  
    return count