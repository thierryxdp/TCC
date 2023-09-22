def conta_frases(frase):
    for i in range (0, len(frase)):
    	if frase[i] in ('!', "?" ,".'" ,"..."):  
        	count = count + 1;
    return count