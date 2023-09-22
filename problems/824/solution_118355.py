def uppCons(frase):
    
    vogais = ['a', 'e', 'i', 'o', 'u'] 
    str.split(frase)
    
    i = 0
    while len(frase)-1 > i :
        if not (frase[i] in vogais):
            str.upper(frase[i])
            
    	i+=1
    str.join(frase, '')
    return frase