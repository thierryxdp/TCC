def uppCons(frase):
    c = ''
    i = 0
    while i<len(frase):
        if frase[i] not in "AEIOUaeiou":
        	letra = str.upper(frase[i])
        	c = c + letra
        i = i + 1
        
    return c