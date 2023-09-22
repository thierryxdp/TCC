def conta_frases(frase):
    
    x = str.count(frase, ".")
    y = str.count(frase, "!")
    z = str.count(frase, "?")
    i = str.count(frase, "...")
    
    if x =! 0 and i =! 0:
        return (x + i -1) + y + z
    
    else: 
    	return x + y + z + i