def conta_frases(frase):
    '''A função contará a quantidade de frases na string inserida pelo usuário.
    
    string-> int'''
    
    x = str.count(frase, ".")
    y = str.count(frase, "!")
    z = str.count(frase, "?")
    i = str.count(frase, "...")
    
    if x != 0 and i != 0:
        return (x - 3*i) + y + z + i
    
    else: 
    	return x + y + z + i