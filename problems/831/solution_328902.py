def lingua_p(string):
    
    
    frase= ' '
    vogais= 'aeiou'
    for letra in string:
        if letra in vogais:
            frase+= letra+p+ letra
        else:
        frase+= letra
        
   	return frase