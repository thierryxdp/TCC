def lingua_p(string):
    
    
    frase= ' '
    vogais= 'aeiou'
    lower= str.lower(string)
    for letra in lower:
        if letra in vogais:
            frase+= letra+p+ letra
       	else:
            frase+= letra
        
   	return frase