def uppCons(frase):
    
    vogais = ''
    i = 0
    
    
    while (i<len(frase)):
        if frase[i] in 'AEIOUaeiou':
            vogais = vogais + frase[i]
        i = i+1
        
    frase = str.upper(frase)
    return frase