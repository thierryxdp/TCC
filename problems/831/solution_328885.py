def lingua_p(string):
    
    
    palavra=''
    vogais='aeiou'
    lower=str.lower(string)
    for letra in lower:
        if letra in vogais:
            palavra+= letra+p+ letra
        else:
            palavra+= letra
   	return palavra