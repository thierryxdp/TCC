def uppCons(frase):
    i = 0
    texto2=''
    while i < len(frase):
        if frase[i] == 'a': 
            texto2 = texto2 + frase[i]
        elif frase[i] == 'e':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'i':
            texto2 = texto2 + frase[i] 
        elif frase[i] == 'o':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'u':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'é':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'ê':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'í':
            texto2 = texto2 + frase[i]    
        elif frase[i] == 'î':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'á':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'â':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'ô':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'ó':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'ú':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'û':
            texto2 = texto2 + frase[i]
        elif frase[i] == 'ã':
            texto2 = texto2 + frase[i]
        
        
        else:
            texto2 = texto2 + str.upper(frase[i])
        i = i +1
        
    return texto2