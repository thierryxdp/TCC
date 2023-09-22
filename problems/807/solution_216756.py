def conta_frases(frase):
    '''Entre com uma frase para contar o numero de frases presente na sua
    String -> Int'''
    
    y=0
    
    b=len(frase)
    
    a=frase.index(frase, "...")
    
    if a>0:
        frase.replace("...", "")
        y+=1
    
    else:
    	x=frase.count('!')
    	z=frase.count('?')
        w=frase.count('.')
    
    	return (x+y+z+w)